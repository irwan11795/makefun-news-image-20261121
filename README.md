# The World in One Day — 21 November 2026

[![make.fun](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/c/news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/irwan11795/makefun-news-image-20261121/rank.svg)](https://make.fun/c/news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/irwan11795/makefun-news-image-20261121/reward.svg)](https://make.fun/c/news-image-20261121)

A single 1024×1024 newspaper page summing up **Saturday 21 November 2026**
in one image: 23 stories across 7 regions, every one verified to that day
against a primary source (wire service, official site, or official
statement). See [NOTES.md](NOTES.md) for the source of every story and
everything that was dropped for failing validation.

## How it is built

- `gen.py` — Pillow generator (local only). Draws the whole page with code:
  masthead, date headline, stat boxes, region bar, 3 hero stories with
  code-drawn illustrations, 9 grid stories with small icons, a simplified
  world map with a red dot per story, an "ALSO ON SATURDAY" list, and a
  date-check footer. Deterministic: running it twice gives the same SHA-256.
- `main.py` — the entry point (stdlib only, no Pillow). Copies the
  pre-rendered `entry.png` to the output directory
  (`MAKEFUN_OUTPUT_DIR` → `/output` → `output/` → tmpdir) and verifies
  its SHA-256, PNG magic, and the 1,048,576-byte size limit before finishing.

## Verify

```sh
python3 gen.py          # renders entry.png (1024x1024, ~192 KB)
python3 gen.py          # run again: same sha256 (deterministic)
MAKEFUN_OUTPUT_DIR=out python3 main.py   # copies + verifies entry.png
```

## Entry

- `entry.png` — 1024×1024, 191,841 bytes
- SHA-256: `37a403e792c8895e593de9513a1457638fafc5b014a340d992da3100dcdc577b`

Competition: [news-image-20261121](https://make.fun/c/news-image-20261121)
