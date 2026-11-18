"""Build the GitHub Pages site in docs/ from the Markdown in content/.

Usage:  python tools/build_site.py
Needs:  pip install markdown
"""
import html
import pathlib
import re
import shutil

import json

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
DOCS = ROOT / "docs"

COVER = "https://pbs.twimg.com/media/HXH4Wh8aMAAWybP.jpg"

PAGES = [
    ("article.html", "01-article-motion-design-with-fable-5.2.md", "Article", "The guide"),
    ("repos.html", "02-thread-20-github-repos-video-editing.md", "20 Repos", "Video editing stack"),
    ("prompts.html", "03-embedded-posts-and-prompt-packs.md", "Prompt packs", "Full prompts"),
]

LINK_MAP = {
    "01-article-motion-design-with-fable-5.2.md": "article.html",
    "02-thread-20-github-repos-video-editing.md": "repos.html",
    "03-embedded-posts-and-prompt-packs.md": "prompts.html",
    "../tools/render.py": "render.py",
    "render.py": "render.py",
}

GALLERY = [
    ("Finished intro", "Two plain-English messages, under 6 minutes", "2121746406381875200/vid/avc1/1920x1080/NV6Js20RBFQ2Vdgv", "2121746406381875200/img/tyMXifONr3G427Ft", "wide"),
    ("One-line prompt", "Impressive, but generic: Fable guessed the brief", "2121746964320841728/vid/avc1/1920x1080/cwT81mc0LNPzsLU2", "2121746964320841728/img/vbVj7cneRMmx5wUW", "wide"),
    ("Director's template", "Six blocks of direction, first try", "2121747161084018688/vid/avc1/1920x1080/SonE7XOMf2OEAitC", "2121747161084018688/img/JwwOeWYhJc45VG6n", "wide"),
    ("After one follow-up", "Two problems, two numbers, one message", "2121747404760518656/vid/avc1/1920x1080/7HW9y5RvGC_kGuVn", "2121747404760518656/img/Qp_AGxk3mpB5e0HV", "wide"),
    ("Vertical Reel", "12 s seamless loop at 120 BPM", "2121747753890177024/vid/avc1/1080x1920/4W38UmmxDL_E9pun", "2121747753890177024/img/sssl0noNoX6VElUQ", "tall"),
    ("One Half (3D)", "A kids cartoon that teaches fractions", "2121215855254196224/vid/avc1/1080x1350/TV3uTpkB9ZA6Z-0R", "2121215855254196224/img/WCYghVlgHjuprsa-", "tall"),
    ("Capybara onsen (3D)", "Five shots, cameras set in meters", "2120496468310237184/vid/avc1/1080x1350/BX-YgJYbxCfCnFiP", "2120496468310237184/img/MqrKAE4MJhVo858D", "tall"),
    ("20-repo stack", "The post's own showcase video", "2122677403998965760/vid/avc1/1080x1350/jbXBov89DPz7X9vj", "2122677403998965760/img/cH2isJgN6nv5UA3f", "tall"),
]

CSS = r"""
:root{--bg:#0e0a09;--panel:#18110f;--panel2:#211715;--line:#33241f;--ink:#f3e7d3;--muted:#b6a48d;
--accent:#e8613c;--accent2:#e9407a;--mustard:#e3a82b;--cream:#efe4cf;--radius:16px}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:radial-gradient(1200px 600px at 80% -10%,#3a1712 0%,transparent 60%),var(--bg);
color:var(--ink);font:17px/1.7 Inter,system-ui,-apple-system,Segoe UI,sans-serif;-webkit-font-smoothing:antialiased}
a{color:var(--mustard);text-decoration:none}a:hover{text-decoration:underline}
.nav{position:sticky;top:0;z-index:10;backdrop-filter:blur(12px);background:rgba(14,10,9,.78);border-bottom:1px solid var(--line)}
.nav .in{max-width:1180px;margin:auto;display:flex;align-items:center;gap:22px;padding:14px 22px;flex-wrap:wrap}
.brand{font-family:'Bricolage Grotesque',Inter,sans-serif;font-weight:800;font-size:19px;color:var(--ink)}
.brand b{background:linear-gradient(90deg,var(--accent),var(--accent2));-webkit-background-clip:text;background-clip:text;color:transparent}
.nav a.l{color:var(--muted);font-size:15px;font-weight:500}.nav a.l.on,.nav a.l:hover{color:var(--ink);text-decoration:none}
.nav .sp{flex:1}
h1,h2,h3,h4{font-family:'Bricolage Grotesque',Inter,sans-serif;line-height:1.15;letter-spacing:-.015em}
h1{font-size:clamp(34px,5vw,56px);margin:.2em 0 .4em}
h2{font-size:30px;margin:2.2em 0 .6em;padding-top:.4em}
h3{font-size:22px;margin:1.8em 0 .5em;color:var(--cream)}h4{font-size:18px;margin:1.6em 0 .4em;color:var(--mustard)}
.grad{background:linear-gradient(90deg,var(--accent),var(--accent2));-webkit-background-clip:text;background-clip:text;color:transparent}
.wrap{max-width:1180px;margin:auto;padding:0 22px}
.layout{display:grid;grid-template-columns:minmax(0,1fr) 240px;gap:56px;max-width:1180px;margin:auto;padding:40px 22px 100px}
.doc{max-width:780px;min-width:0}
.toc{position:sticky;top:84px;align-self:start;max-height:calc(100vh - 110px);overflow:auto;font-size:14px;border-left:1px solid var(--line);padding-left:18px}
.toc b{display:block;color:var(--muted);font-size:12px;letter-spacing:.12em;text-transform:uppercase;margin-bottom:10px}
.toc a{display:block;color:var(--muted);padding:4px 0;line-height:1.35}.toc a:hover{color:var(--ink);text-decoration:none}
@media(max-width:980px){.layout{grid-template-columns:1fr}.toc{display:none}}
p,li,td{color:#eadcc6;overflow-wrap:anywhere}strong{color:var(--ink)}
hr{border:0;height:1px;background:linear-gradient(90deg,transparent,var(--line),transparent);margin:48px 0}
blockquote{margin:22px 0;padding:14px 20px;border-left:3px solid var(--accent);background:var(--panel);border-radius:0 12px 12px 0;color:var(--muted)}
blockquote p{margin:.3em 0;color:#e2d3bd}
code{font-family:'JetBrains Mono',ui-monospace,Menlo,monospace;font-size:.88em;background:var(--panel2);border:1px solid var(--line);padding:.1em .4em;border-radius:6px}
pre{position:relative;background:#120d0c;border:1px solid var(--line);border-radius:var(--radius);padding:20px 22px;overflow:auto;line-height:1.55}
pre code{background:none;border:0;padding:0;font-size:13.5px;color:#f1e2cb;white-space:pre-wrap;word-break:break-word}
.copy{position:absolute;top:10px;right:10px;font:600 12px Inter,sans-serif;color:var(--ink);background:var(--panel2);border:1px solid var(--line);border-radius:8px;padding:6px 10px;cursor:pointer;opacity:.85}
.copy:hover{opacity:1;border-color:var(--accent)}
table{width:100%;border-collapse:separate;border-spacing:0;margin:22px 0;font-size:15px;border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;display:block;overflow-x:auto}
th,td{padding:11px 14px;text-align:left;vertical-align:top;border-bottom:1px solid var(--line)}
th{background:var(--panel2);color:var(--cream);font-weight:600;white-space:nowrap}
tr:last-child td{border-bottom:0}tbody tr:nth-child(even) td{background:rgba(255,255,255,.015)}
img{max-width:100%;border-radius:12px}
figure{margin:30px 0}figure img{display:block;margin:auto;border:1px solid var(--line)}
figure.video video{display:block;width:100%;border-radius:var(--radius);border:1px solid var(--line);background:#000;box-shadow:0 20px 60px rgba(0,0,0,.45)}
figure.video.tall video{max-height:78vh;width:auto;max-width:100%;margin:auto}
figcaption{text-align:center;font-size:14px;color:var(--muted);margin-top:10px}
figcaption a{font-weight:600}
.hero{position:relative;border-radius:28px;overflow:hidden;margin:36px 0 18px;border:1px solid var(--line)}
.hero img{display:block;width:100%;border-radius:0}
.hero-copy{padding:40px 0 10px;max-width:820px}
.hero-copy p.lead{font-size:20px;color:var(--muted)}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:14px;margin:30px 0}
.stat{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);padding:18px}
.stat b{display:block;font:800 30px 'Bricolage Grotesque',Inter,sans-serif;color:var(--ink)}
.stat span{color:var(--muted);font-size:14px}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px;margin:26px 0 10px}
.card{display:block;background:linear-gradient(180deg,var(--panel2),var(--panel));border:1px solid var(--line);border-radius:22px;padding:26px;color:var(--ink);transition:.2s}
.card:hover{transform:translateY(-3px);border-color:var(--accent);text-decoration:none}
.card .k{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--accent)}
.card h3{margin:.4em 0 .3em;color:var(--ink)}.card p{color:var(--muted);margin:0;font-size:15px}
.gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:18px;margin-top:22px}
.gallery .g{background:var(--panel);border:1px solid var(--line);border-radius:18px;overflow:hidden}
.gallery video{display:block;width:100%;aspect-ratio:16/9;object-fit:cover;background:#000}
.gallery .g.tall video{aspect-ratio:4/5}
.gallery .t{padding:12px 14px}.gallery .t b{display:block}.gallery .t span{font-size:13.5px;color:var(--muted)}
.foot{border-top:1px solid var(--line);color:var(--muted);font-size:13.5px;text-align:center;padding:30px 22px 50px}
.pill{display:inline-block;font-size:12.5px;padding:4px 10px;border-radius:999px;border:1px solid var(--line);color:var(--muted);margin:0 6px 6px 0}
"""

JS = r"""
document.querySelectorAll('pre').forEach(pre=>{const b=document.createElement('button');b.className='copy';b.textContent='Copy';
b.onclick=()=>{navigator.clipboard.writeText(pre.innerText.replace(/^Copy\n?/,'')).then(()=>{b.textContent='Copied';setTimeout(()=>b.textContent='Copy',1400)})};pre.prepend(b)});
"""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@600;800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">')


def shell(title, active, body):
    links = '<a class="l{on}" href="index.html">Home</a>'.format(on=" on" if active == "index.html" else "")
    for fname, _, label, _ in PAGES:
        links += f'<a class="l{" on" if active == fname else ""}" href="{fname}">{label}</a>'
    links += f'<a class="l{" on" if active == "sources.html" else ""}" href="sources.html">Sources</a>'
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="robots" content="noindex">{FONTS}<style>{CSS}</style></head><body>
<nav class="nav"><div class="in"><a class="brand" href="index.html">Fable <b>5.2</b> Motion Archive</a><span class="sp"></span>{links}</div></nav>
{body}
<div class="foot">All content © its authors (@anstapnever; @claudeai for the launch post). Archived 18 Nov 2026 for personal reference.</div>
<script>{JS}</script></body></html>"""


VID_BLOCK = re.compile(r'<p align="center"><a href="([^"]+)"><img src="([^"]+)" width="\d+" alt="([^"]*)"></a><br>\s*<sub>(.*?)</sub></p>', re.S)
IMG_BLOCK = re.compile(r'<p align="center"><img src="([^"]+)" width="\d+" alt="([^"]*)"></p>')


def video_fig(m):
    mp4, poster, alt, cap = m.groups()
    tall = any(k in mp4 for k in ("1080x1920", "1080x1350", "v6-", "v7-", "v9-", "v10-"))
    cap = cap.replace("▶ ", "")
    return (f'<figure class="video{" tall" if tall else ""}"><video controls playsinline preload="none" poster="{poster}">'
            f'<source src="{mp4}" type="video/mp4"></video><figcaption>{cap}</figcaption></figure>')


URL = re.compile(r'(?<![("<=\[/])(https?://[^\s)<>|`*]+[^\s)<>|`*.,])')


def linkify(text):
    out, fence = [], False
    for line in text.split("\n"):
        if line.startswith("```"):
            fence = not fence
        elif not fence and not line.lstrip().startswith("<"):
            line = URL.sub(r"<\1>", line)
        out.append(line)
    return "\n".join(out)


def render_md(text):
    text = linkify(text)
    text = VID_BLOCK.sub(video_fig, text)
    text = IMG_BLOCK.sub(lambda m: f'<figure><img src="{m.group(1)}" alt="{m.group(2)}"></figure>', text)
    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "sane_lists"],
                           extension_configs={"toc": {"toc_depth": "2-3"}})
    out = md.convert(text)
    for src, dst in LINK_MAP.items():
        out = out.replace(f'href="{src}"', f'href="{dst}"')
    out = out.replace('href="../content/', 'href="').replace('href="../tools/render.py"', 'href="render.py"')
    for src, dst in LINK_MAP.items():
        out = out.replace(f'href="{src}"', f'href="{dst}"')
    return out, md.toc_tokens


def toc_html(tokens):
    items = []
    for t in tokens:
        items.append(f'<a href="#{t["id"]}">{t["name"]}</a>')
        for c in t.get("children", []):
            items.append(f'<a href="#{c["id"]}" style="padding-left:12px">{c["name"]}</a>')
    return "<b>On this page</b>" + "".join(items)


def localize_html(out):
    """Point remote media URLs at docs/media/ copies when they exist (after tools/fetch_media.py)."""
    out = out.replace("../docs/media/", "media/").replace("docs/media/", "media/")
    manifest = ROOT / "sources" / "media-manifest.json"
    if manifest.exists():
        for item in json.loads(manifest.read_text())["files"]:
            if (ROOT / item["path"]).exists():
                local = "media/" + pathlib.Path(item["path"]).name
                out = out.replace(item["original"], local).replace(item["original"].replace("&", "&amp;"), local)
    return out


def write(path, text):
    path.write_text(localize_html(text))


def build():
    DOCS.mkdir(exist_ok=True)
    for fname, src, label, _ in PAGES:
        text = (CONTENT / src).read_text()
        body, tokens = render_md(text)
        flat = tokens[0]["children"] if tokens and tokens[0].get("level") == 1 else tokens
        page = f'<div class="layout"><article class="doc">{body}</article><aside class="toc">{toc_html(flat)}</aside></div>'
        title = re.search(r"^# (.+)$", text, re.M).group(1)
        write(DOCS / fname, shell(title, fname, page))

    src_text = (ROOT / "sources" / "SOURCES.md").read_text()
    body, tokens = render_md(src_text)
    flat = tokens[0]["children"] if tokens and tokens[0].get("level") == 1 else tokens
    write(DOCS / "sources.html", shell("Master sources", "sources.html",
        f'<div class="layout"><article class="doc" style="max-width:100%">{body}</article><aside class="toc">{toc_html(flat)}</aside></div>'))

    gallery = ""
    for t, s, vid, th, shape in GALLERY:
        gallery += (f'<div class="g {shape}"><video controls playsinline preload="none" '
                    f'poster="https://pbs.twimg.com/amplify_video_thumb/{th}.jpg">'
                    f'<source src="https://video.twimg.com/amplify_video/{vid}.mp4?tag=29" type="video/mp4"></video>'
                    f'<div class="t"><b>{t}</b><span>{s}</span></div></div>')
    home = f"""<div class="wrap">
<div class="hero"><img src="{COVER}" alt="Motion Design with Fable 5.2"></div>
<div class="hero-copy">
<span class="pill">Archived 18 Nov 2026</span><span class="pill">by @anstapnever</span><span class="pill">10 videos · 9 prompts · 20 repos</span>
<h1>Motion design with <span class="grad">Fable 5.2</span>, archived in full.</h1>
<p class="lead">The complete guide from zero to your first MP4, the 20 open-source repos that turn Fable into a video editing studio, and both prompt packs, word for word.</p>
</div>
<div class="stats">
<div class="stat"><b>10 min</b><span>to your first video</span></div>
<div class="stat"><b>6 blocks</b><span>in the director's template</span></div>
<div class="stat"><b>$2.39</b><span>for a one-message fix</span></div>
<div class="stat"><b>20</b><span>GitHub repos in the stack</span></div>
</div>
<div class="cards">
<a class="card" href="article.html"><span class="k">01 · Article</span><h3>The guide</h3><p>Setup, the director's template, 12 fix-it phrases, vertical video, rendering, music and 10 beginner mistakes.</p></a>
<a class="card" href="repos.html"><span class="k">02 · Post</span><h3>20-repo editing stack</h3><p>Edit, captions, audio, AI FX and export, with every link expanded.</p></a>
<a class="card" href="prompts.html"><span class="k">03 · Prompt packs</span><h3>Cartoon + capybara</h3><p>The 1146-word and 822-word prompts, cost tables, 10 kids lessons and templates.</p></a>
<a class="card" href="sources.html"><span class="k">04 · Sources</span><h3>Master sources</h3><p>Every original URL, how it was captured, and the full media inventory.</p></a>
</div>
<h2>Watch the results</h2>
<div class="gallery">{gallery}</div>
<h2>Downloads</h2>
<div class="cards">
<a class="card" href="media/prompt-pack-one-half.pdf"><span class="k">PDF · 5 pages</span><h3>One Half prompt pack</h3><p>The original designed PDF.</p></a>
<a class="card" href="media/prompt-pack-capybara-onsen.pdf"><span class="k">PDF · 4 pages</span><h3>Capybara Onsen prompt pack</h3><p>The original designed PDF.</p></a>
<a class="card" href="render.py"><span class="k">Python</span><h3>render.py</h3><p>The author's frame-perfect HTML-to-MP4 renderer.</p></a>
</div>
</div>"""
    write(DOCS / "index.html", shell("Fable 5.2 Motion Design Archive", "index.html", home))
    shutil.copy(ROOT / "tools" / "render.py", DOCS / "render.py")
    (DOCS / ".nojekyll").write_text("")
    print("built:", sorted(p.name for p in DOCS.iterdir()))


if __name__ == "__main__":
    build()
