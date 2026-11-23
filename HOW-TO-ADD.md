# How a new X post becomes an entry

Send Claude the X link and say "add this to the Fable repo". Claude does the rest; this file records the steps so the result is always the same.

1. **Capture with Apify.** Articles: `xquik/x-article-scraper` (read the `contents` blocks, which hold the videos and embedded posts). Posts: `xquik/x-tweet-scraper` (use `noteTweet.text` and the expanded links). Replies: `apidojo/tweet-scraper` with `conversationIds`. Follow every embedded post and every linked file.
2. **Back up the media.** Run `automa-flow/parallel-bulk-file-downloader` on every video (highest-bitrate MP4), poster, image and PDF.
3. **Write the entry.** Articles: run `tools/x_article_to_md.py` on the scraped JSON. Posts: write `content/NN-short-title.md`: metadata block, verbatim text, videos as thumbnail blocks, images in place, links expanded.
4. **Register it.** Add the entry to `sources/entries.json` (id, file, title, kind, author, handle, date, source, cover, summary, tags) and its media rows to `sources/media-manifest.json` (path, original, mirror, bytes, kind, entry, title, poster).
5. **Log the sources.** Add the URLs and capture method to `sources/SOURCES.md`.
6. **Push.** The workflow downloads the media, switches links to local copies and rebuilds the README, REPOS.md and the website.

Rules: wording stays verbatim; no media is left only on X; every new repo shows up in REPOS.md automatically.
