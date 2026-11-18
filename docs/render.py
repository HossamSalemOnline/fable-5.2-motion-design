# render.py: turns an animated HTML page into a smooth MP4, frame by frame.
# Setup once:  pip install playwright   (plus Google Chrome and ffmpeg, see the article)
# Use:         python render.py index.html 10            (file, seconds)
#              python render.py index.html 12 1080 1920  (vertical)
import sys, subprocess, pathlib
from playwright.sync_api import sync_playwright

page_file = pathlib.Path(sys.argv[1]).resolve()
SECONDS = float(sys.argv[2]) if len(sys.argv) > 2 else 10
W = int(sys.argv[3]) if len(sys.argv) > 3 else 1920
H = int(sys.argv[4]) if len(sys.argv) > 4 else 1080
FPS = 60
out = page_file.with_suffix(".mp4")

# A fake clock: the page thinks time passes exactly 1/60 s per frame,
# so no frame is ever dropped, however slow your computer is.
CLOCK = """
(() => {
  let now = 0; const start = Date.now(); const RealDate = Date;
  performance.now = () => now;
  Date.now = () => start + now;
  window.Date = class extends RealDate {
    constructor(...a) { a.length ? super(...a) : super(start + now); }
    static now() { return start + now; }
  };
  let queue = [];
  window.requestAnimationFrame = cb => { queue.push(cb); return queue.length; };
  window.cancelAnimationFrame = () => {};
  window.__tick = ms => { now += ms; const q = queue; queue = []; q.forEach(cb => cb(now)); };
})();
"""

ffmpeg = subprocess.Popen([
    "ffmpeg", "-y", "-loglevel", "error",
    "-f", "image2pipe", "-framerate", str(FPS), "-i", "-",
    "-c:v", "libx264", "-crf", "16", "-preset", "slow", "-pix_fmt", "yuv420p",
    "-movflags", "+faststart", str(out)], stdin=subprocess.PIPE)

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", args=["--enable-gpu", "--ignore-gpu-blocklist"])  # uses your own Google Chrome
    page = browser.new_page(viewport={"width": W, "height": H})
    page.add_init_script(CLOCK)
    page.goto(page_file.as_uri())
    page.wait_for_load_state("networkidle")
    page.evaluate("document.fonts.ready")
    page.evaluate("window.__tick(0)")
    frames = int(SECONDS * FPS)
    for i in range(frames):
        page.evaluate(f"window.__tick({1000 / FPS})")
        ffmpeg.stdin.write(page.screenshot(type="jpeg", quality=95))
        if i % FPS == 0:
            print(f"{i // FPS + 1} / {int(SECONDS)} s")
    browser.close()

ffmpeg.stdin.close(); ffmpeg.wait()
print("done:", out)
