---
name: subtitle-zh-en-pipeline
description: Translate a Chinese film subtitle/dialogue list (one subtitle per line, or SRT) into natural, on-screen-ready English. Orchestrates six open-source skills (baoyu-translate, subtitle-translation, srt-translator, alterlab-cdm-subtitle-loc, humanizer, verification-before-completion) and the subtitle_check.py script. Use when the user asks to translate Chinese subtitles or a dialogue list into English.
license: MIT
---

# Chinese → English Subtitle Pipeline

Written for this package (week6_skills_package). It decides which skill applies at
each step; the skills themselves are vendored unchanged next to this file.

Paths below are relative to `B_with_skills/`.

## Inputs

- `SOURCE`: Chinese subtitle file, one subtitle per line (or SRT entries).
- `BRIEF`: short film background (characters, genre, register).
- `OUT_DIR`: where intermediate files go (e.g. `work/`).

The run is non-interactive. Do not stop to ask the user anything: preferences come
from `.baoyu-skills/baoyu-translate/EXTEND.md`, which satisfies baoyu-translate's
first-time setup.

## Hard rules (from srt-translator + alterlab-cdm-subtitle-loc)

1. **Structure is frozen.** Output has exactly as many lines as `SOURCE`; line N
   translates line N. Never merge, split or reorder entries. Timecodes, if present,
   are copied byte-for-byte.
2. One subtitle ≤ 84 characters (2 × 42). Aim for ≤ 42 so it fits on one line.
3. Estimated reading speed ≤ 17 CPS. The source has no timecodes, so English should
   be about as short as the Chinese is quick.
4. Plain ASCII punctuation: no em/en dashes, no curly quotes.
5. Same Chinese term → same English term every time (glossary), unless a character
   is deliberately varying it.

## Steps

### 1. Analyse and build the glossary — `baoyu-translate` (refined mode)

Read `skills/baoyu-translate/SKILL.md` and `references/refined-workflow.md`.
Skip the chunking script (input is far below 4000 words) and the image-language
pass (no images). Write:

- `OUT_DIR/01-analysis.md`: who speaks each line where it can be inferred,
  register, dialect and slang, jokes and teasing, onomatopoeia, numbers/countdowns.
- `OUT_DIR/glossary.md` (markdown table `| from | to | note |`): recurring terms,
  nicknames, insults and objects, with one chosen rendering each.
- `OUT_DIR/02-prompt.md`: the assembled translation brief (BRIEF + analysis +
  glossary + the hard rules above + `skills/subtitle-translation` core rules).

### 2. Draft — `subtitle-translation` + `srt-translator`

Translate following `02-prompt.md` into `OUT_DIR/03-draft.txt` (plain lines, same
count as SOURCE). From `subtitle-translation`: spoken naturalness over literal
structure, kids should sound like kids, short lines, keep the jokes and the fear.
From `srt-translator`: localize rather than translate word for word; keep structure.

### 3. Measure the draft — `scripts/subtitle_check.py`

```bash
python3 scripts/subtitle_check.py SOURCE OUT_DIR/03-draft.txt --terms scripts/eval_terms.json > OUT_DIR/03-draft-check.md
```

### 4. Critique — `baoyu-translate` review + `humanizer` + `alterlab-cdm-subtitle-loc`

Write `OUT_DIR/04-critique.md` (diagnosis only, no rewriting yet), covering:

- accuracy against the Chinese (baoyu-translate critique checklist),
- translationese / AI tells, using the `humanizer` pattern list. Apply the patterns
  that fit dialogue (stock AI words, staged openers, inflated wording, dashes,
  over-tidy grammar, filler); ignore prose-only ones (bold labels, headings),
- subtitle craft from `alterlab-cdm-subtitle-loc`: line length, reading speed,
  character voice consistency, grammatical units,
- every hard or soft item in `03-draft-check.md`.

### 5. Revise and polish

Apply the critique → `OUT_DIR/05-revision.txt`, then a final read-aloud polish →
`OUT_DIR/translation.txt`. Copy the final file to `result_en.txt`.

### 6. Verify before claiming done — `verification-before-completion`

Run the checker on the final file and save its full output:

```bash
python3 scripts/subtitle_check.py SOURCE result_en.txt --terms scripts/eval_terms.json > check_report.md; echo "exit=$?"
```

Exit code must be 0 (no hard issues). If not, fix and re-run. Report what the
checker printed, including any soft notes you chose to keep and why. Do not say
"done" without this fresh output.
