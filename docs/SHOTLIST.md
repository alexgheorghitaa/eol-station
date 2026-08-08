# Screenshot shot list

Eight figures are referenced from `README.md`. Each one is currently wrapped in an HTML
comment so the README renders cleanly without them.

**To publish a figure:**

1. Take the shot as described below.
2. Save it in `docs/img/` with the exact filename given.
3. In `README.md`, find the matching `<!-- FIGURE n … -->` block and delete the two
   comment markers (`<!-- FIGURE n — uncomment once …` and the closing `-->`), leaving
   only the `![…](…)` line.

**Before every shot:**

- Press <kbd>Ctrl</kbd>+<kbd>U</kbd> on any block diagram — Clean Up Diagram. An untidy
  diagram in documentation reads as an untidy engineer.
- Close the Context Help window (<kbd>Ctrl</kbd>+<kbd>H</kbd> toggles it) and any
  floating palettes. They are visible in every screenshot you have sent me so far.
- Crop to the content. No taskbar, no Windows title bar, no desktop wallpaper.
- <kbd>Win</kbd>+<kbd>Shift</kbd>+<kbd>S</kbd> gives you a rectangular capture directly.
- PNG, not JPEG. Text stays sharp and the files stay small.
- Target roughly 1400–1800 px wide. Wider than that and GitHub downscales it into mush.

---

## 01 — Sequencer front panel, mid-run

**File:** `docs/img/01-sequencer-panel.png` · **Needs:** session 5
**This is the hero image — the first thing anyone sees. Spend the most time on it.**

Run `station/Run_One.vi` on **seed 125** — an insulation fault, so the sequence aborts and
the panel shows real content rather than four green lights. Capture the front panel showing:

- `state` and `verdict`
- the three verdict LEDs, with DUT FAIL lit
- the `results` table expanded enough that **all rows are visible at once** — including
  the rows marked `Skipped`
- `serial`, `duration ms`, `first failed step`

Drag the results array indicator taller before running so no scrolling is needed.

---

## 02 — Sequencer block diagram

**File:** `docs/img/02-sequencer-diagram.png` · **Needs:** session 5

The whole While loop with the Case Structure visible. Set the case selector to **`Iso`**
— it is the most instructive case, because it contains both the normal path and the abort
that jumps to Evaluate.

<kbd>Ctrl</kbd>+<kbd>U</kbd> first. If it does not fit on screen, use
**View ▸ Zoom Out** rather than scrolling and stitching.

---

## 03 — Simulator console

**File:** `docs/img/03-simulator-console.png` · **Needs:** available now

The Python terminal during a full sequence. Capture from `listening on 127.0.0.1:5025`
down through a run — the `client connected` line and 15–20 command/reply lines. Include
at least one `ERR,` reply if you can (run a faulty seed) so the error-as-data point is
visible.

Widen the terminal window first so no line wraps.

---

## 04 — HTML report, passing unit

**File:** `docs/img/04-report-pass.png` · **Needs:** session 6

Open `reports/` in a browser. **Seed 123** passes everything. Capture the whole page —
banner, serial, the step table with values, limits, margins and durations.

Browser zoom to 90% if it does not fit in one screen. Hide the browser chrome (F11) or
crop it out.

---

## 05 — HTML report, failing unit

**File:** `docs/img/05-report-fail.png` · **Needs:** session 6

Same, on **seed 125** (insulation fault, aborts). The point of this figure is the contrast
with 04: the failed row, its negative margin, and the rows marked `Skipped` with the
reason in the note column. Make sure all three are in frame.

If you would rather show a cell failure than an insulation failure, use **seed 120** —
but then there are no `Skipped` rows, because a bad cell does not abort the sequence.

---

## 06 — Batch metrics

**File:** `docs/img/06-batch-metrics.png` · **Needs:** session 7

`station/Batch.vi` front panel after a complete 30-unit run:

- FPY, tester availability, units started
- the first-failure Pareto
- the golden-unit gate indicator showing it passed

If the Pareto is a plain array rather than a chart, that is fine — put a Bar Chart on it
first if you have twenty spare minutes, since this figure is the one a manufacturing
engineer looks at longest.

---

## 07 — Burst vs per-cell comparison

**File:** `docs/img/07-compare-ocv.png` · **Needs:** session 8

`station/Compare_OCV.vi` front panel showing `max abs delta V`, the `decoder verified`
LED lit, and both timing numbers. This is the figure that proves the cycle-time claim,
so the two durations and the deviation must all be legible.

---

## 08 — Project Explorer

**File:** `docs/img/08-project-explorer.png` · **Needs:** available now

The LabVIEW Project Explorer window with `lib/` and `station/` **expanded**, so every VI
and `.ctl` is listed. Collapse anything irrelevant. This one takes thirty seconds and it
shows structure at a glance.

---

## When all eight are in

Delete this file — `git rm docs/SHOTLIST.md`. It is scaffolding, not documentation.
