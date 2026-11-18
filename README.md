<div align="center">

<img src="https://pbs.twimg.com/media/HXH4Wh8aMAAWybP.jpg" width="100%" alt="Motion Design with Fable 5.2">

# Fable 5.2 Motion Design Archive

**A full, faithful archive of @anstapnever's Fable 5.2 motion design guide, the 20-repo video editing stack, and both prompt packs.**

![Captured](https://img.shields.io/badge/captured-18%20Nov%202026-E8613C?style=flat-square)
![Videos](https://img.shields.io/badge/videos-10-D9541E?style=flat-square)
![Prompts](https://img.shields.io/badge/copy--ready%20prompts-9-E3A82B?style=flat-square)
![Repos](https://img.shields.io/badge/GitHub%20repos-20-2B1B12?style=flat-square)
![Source](https://img.shields.io/badge/source-X%20%2B%20Google%20Drive-1E140E?style=flat-square)

[**Read the article**](content/01-article-motion-design-with-fable-5.2.md) · [**20 repos**](content/02-thread-20-github-repos-video-editing.md) · [**Prompt packs**](content/03-embedded-posts-and-prompt-packs.md) · [**Master sources**](sources/SOURCES.md) · [**Website**](docs/index.html)

</div>

---

## Watch first

| Finished intro (two messages) | One-line prompt (generic) | Director's template (on brief) |
|:---:|:---:|:---:|
| [![Finished intro](https://pbs.twimg.com/amplify_video_thumb/2121746406381875200/img/tyMXifONr3G427Ft.jpg)](https://video.twimg.com/amplify_video/2121746406381875200/vid/avc1/1920x1080/NV6Js20RBFQ2Vdgv.mp4?tag=29) | [![One-line result](https://pbs.twimg.com/amplify_video_thumb/2121746964320841728/img/vbVj7cneRMmx5wUW.jpg)](https://video.twimg.com/amplify_video/2121746964320841728/vid/avc1/1920x1080/cwT81mc0LNPzsLU2.mp4?tag=29) | [![Template result](https://pbs.twimg.com/amplify_video_thumb/2121747161084018688/img/JwwOeWYhJc45VG6n.jpg)](https://video.twimg.com/amplify_video/2121747161084018688/vid/avc1/1920x1080/SonE7XOMf2OEAitC.mp4?tag=29) |
| **After one follow-up** | **Side by side** | **Vertical Reel (9:16 loop)** |
| [![Follow-up result](https://pbs.twimg.com/amplify_video_thumb/2121747404760518656/img/Qp_AGxk3mpB5e0HV.jpg)](https://video.twimg.com/amplify_video/2121747404760518656/vid/avc1/1920x1080/7HW9y5RvGC_kGuVn.mp4?tag=29) | [![Side by side](https://pbs.twimg.com/amplify_video_thumb/2121747275059965952/img/D8eqMiGpUbv383AT.jpg)](https://video.twimg.com/amplify_video/2121747275059965952/vid/avc1/1920x800/UoD2B2tykucHTh0W.mp4?tag=29) | [![Vertical Reel](https://pbs.twimg.com/amplify_video_thumb/2121747753890177024/img/sssl0noNoX6VElUQ.jpg)](https://video.twimg.com/amplify_video/2121747753890177024/vid/avc1/1080x1920/4W38UmmxDL_E9pun.mp4?tag=29) |
| **"One Half" kids cartoon (3D)** | **Capybara onsen (3D)** | **20-repo stack** |
| [![One Half](https://pbs.twimg.com/amplify_video_thumb/2121215855254196224/img/WCYghVlgHjuprsa-.jpg)](https://video.twimg.com/amplify_video/2121215855254196224/vid/avc1/1080x1350/TV3uTpkB9ZA6Z-0R.mp4?tag=29) | [![Capybara](https://pbs.twimg.com/amplify_video_thumb/2120496468310237184/img/MqrKAE4MJhVo858D.jpg)](https://video.twimg.com/amplify_video/2120496468310237184/vid/avc1/1080x1350/BX-YgJYbxCfCnFiP.mp4?tag=29) | [![20 repos](https://pbs.twimg.com/amplify_video_thumb/2122677403998965760/img/cH2isJgN6nv5UA3f.jpg)](https://video.twimg.com/amplify_video/2122677403998965760/vid/avc1/1080x1350/jbXBov89DPz7X9vj.mp4?tag=29) |

<sub>Click any thumbnail to play the MP4. All 24 media files are stored in this repo under <code>docs/media/</code>, so nothing depends on X staying online.</sub>

---

## What's inside

| | File | What you get |
|---|---|---|
| 📘 | [**The article**](content/01-article-motion-design-with-fable-5.2.md) | The guide in full: how it works, what it costs, setup on the Claude app and Claude Code, the director's template, 12 fix-it phrases, vertical video, rendering to MP4, adding music, 10 beginner mistakes. |
| 🧰 | [**20 repos**](content/02-thread-20-github-repos-video-editing.md) | The video editing stack, every link expanded, grouped by stage, plus the public replies. |
| 🎬 | [**Prompt packs**](content/03-embedded-posts-and-prompt-packs.md) | Both PDFs in full: the 1146-word "One Half" cartoon prompt and the 822-word capybara prompt, Fable vs Opus cost tables, 10 kids lessons and two fill-in templates. |
| 📄 | [**Original PDFs**](docs/media/) | Both prompt packs as the author designed them: [One Half](docs/media/prompt-pack-one-half.pdf) (5 pages) and [Capybara Onsen](docs/media/prompt-pack-capybara-onsen.pdf) (4 pages). |
| 🗂 | [**Master sources**](sources/SOURCES.md) | Every original URL, how it was captured, and an inventory of all 12 media items. |
| ⚙️ | [**render.py**](tools/render.py) | The author's frame-perfect HTML-to-MP4 renderer. |
| 🌐 | [**Website**](docs/index.html) | The same content as a designed site with videos playing inline. Turn on GitHub Pages from `/docs` to publish it. |

---

## The director's template

The core idea of the guide: give Fable a brief, not an adjective.

```text
Make a [length]-second animated video as one HTML file I can open in Chrome. Everything is drawn in code: no images, no video files. Do it in one go without asking me questions.

WHAT: [what it is and who it's for, one sentence]

SIZE: [1920x1080 for YouTube and X, 1080x1920 for Reels and TikTok], 60 fps. [It plays once and holds the last frame / It loops with no seam.]

LOOK: background [color + hex code], text [color + hex], one accent [color + hex]. Font: [style, e.g. a bold rounded sans-serif from Google Fonts].

TIMELINE:
[0.0-1.0 s]: [what happens]
[1.0-3.0 s]: [what happens]
[...]: [one line per moment, until the end]

MOTION: nothing moves in a straight line at constant speed. Entrances ease out, exits ease in. Every bounce settles within 0.4 s.
```

## The 20-repo stack at a glance

| Stage | Repos |
|---|---|
| **Edit** | [DaVinci Resolve MCP](https://github.com/samuelgursky/davinci-resolve-mcp) · [auto-editor](https://github.com/WyattBlue/auto-editor) · [PySceneDetect](https://github.com/Breakthrough/PySceneDetect) · [MoviePy](https://github.com/Zulko/moviepy) · [Remotion](https://github.com/remotion-dev/remotion) · [video-use](https://github.com/browser-use/video-use) |
| **Captions** | [faster-whisper](https://github.com/SYSTRAN/faster-whisper) · [WhisperX](https://github.com/m-bain/whisperX) · [AutoSubs](https://github.com/tmoroney/auto-subs) · [FunClip](https://github.com/modelscope/FunClip) |
| **Audio** | [Demucs](https://github.com/adefossez/demucs) · [DeepFilterNet](https://github.com/Rikorose/DeepFilterNet) |
| **AI FX** | [SAM 2](https://github.com/facebookresearch/sam2) · [RobustVideoMatting](https://github.com/PeterL1n/RobustVideoMatting) · [ProPainter](https://github.com/sczhou/ProPainter) · [video-subtitle-remover](https://github.com/YaoFANGUK/video-subtitle-remover) · [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) · [LatentSync](https://github.com/bytedance/LatentSync) |
| **Export** | [LosslessCut](https://github.com/mifi/lossless-cut) · [FFmpeg](https://github.com/FFmpeg/FFmpeg) |

<sub>The grouping is mine, based on the post's "edit. captions. audio. AI FX. export." line.</sub>

## Cost reference (API prices, from the author's session logs)

| Video | Model | Time | Cost |
|---|---|---|---|
| YouTube intro, one line | Fable 5.2 | 6m 56s | $3.65 |
| YouTube intro, director's template | Fable 5.2 | 2m 22s | $2.81 |
| Same intro, one follow-up | Fable 5.2 | 3m 21s | $2.39 |
| Vertical post for Reels | Fable 5.2 | 5m 16s | $3.03 |
| 30 s kids cartoon in 3D | Fable 5.2 / Opus 5.5 | 11m 11s / 28m 53s | $9.34 / $7.12 |
| 24 s capybara scene in 3D | Fable 5.2 / Opus 5.5 | 26m 47s / 27m 37s | $11.32 / $6.39 |

## Repository layout

```text
.
├── README.md                  ← you are here
├── content/
│   ├── 01-article-motion-design-with-fable-5.2.md
│   ├── 02-thread-20-github-repos-video-editing.md
│   └── 03-embedded-posts-and-prompt-packs.md
├── sources/
│   ├── SOURCES.md             ← master source list and media inventory
│   └── media-manifest.json    ← every media file: original URL + Apify backup
├── tools/
│   ├── render.py              ← HTML → MP4, frame by frame
│   ├── build_site.py          ← rebuilds docs/ from content/
│   └── fetch_media.py         ← downloads all media into docs/media/
├── .github/workflows/
│   └── fetch-media.yml        ← runs fetch_media + build_site on every push
└── docs/                      ← GitHub Pages site + docs/media/ (videos, images, PDFs)
```

---

<div align="center">
<sub>All content © its authors (@anstapnever; @claudeai for the launch post). Archived 18 Nov 2026 for personal reference. Keep this repository private unless you have permission to republish.</sub>
</div>
