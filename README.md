# board-notes

This repo stores lightboard notes and images from [Whitney Lee](https://github.com/wiggitywhitney)'s shows:

- **Thunder** (with Viktor Farcic) — deep-dive technical episodes
- **Datadog Illuminated** — engineering stories from Datadog builders  
- **⚡️Enlightning** — cloud native community episodes

## Purpose

Board images and markdown transcripts live here so they can be embedded in [GitHub gists](https://gist.github.com/wiggitywhitney) via stable public raw URLs. Gists are the shareable, bookmarkable reference artifact linked from YouTube descriptions and social posts.

## Directory Structure

```
board-notes/
  thunder/
    ep-slug/
      board.jpg      ← color-corrected lightboard image
      notes.md       ← verbatim board text (source for gist)
  datadog-illuminated/
    episode-slug/
      board.jpg
      notes.md
  enlightning/
    ep-slug/
      notes.md       ← references Thunder's board image URL (no duplicate image stored)
```

## Board Images

Raw URLs for embedding (stable, publicly accessible):

```
https://raw.githubusercontent.com/wiggitywhitney/board-notes/main/{show}/{episode-slug}/board.{ext}
```

## Color Correction

Raw lightboard images are processed with `sips` before committing to correct for brightness and green cast introduced by the lightboard setup. The exact correction parameters are recorded in the [/board-gist skill PRD](https://github.com/wiggitywhitney/journal/issues/58).
