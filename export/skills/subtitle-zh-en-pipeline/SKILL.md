---
name: 字幕翻译
description: 字幕翻译 (subtitle-zh-en-pipeline). Translate a Chinese film subtitle/dialogue list (one subtitle per line, or SRT) into natural, on-screen-ready English. Orchestrates six open-source skills (baoyu-translate, subtitle-translation, srt-translator, alterlab-cdm-subtitle-loc, humanizer, verification-before-completion) and a bundled subtitle checker. Use when the user says 字幕翻译 or asks to translate Chinese subtitles, 字幕, or a dialogue list into English.
license: MIT
---

# Chinese → English Subtitle Pipeline

From week6_skills_package (github.com/Garyklay28/week6_skills_package). This skill
decides which skill applies at each step; the six skills it uses are installed as
sibling folders next to this one. `<skill-dir>` below means this SKILL.md's folder,
and `<skills>` means its parent folder.

## Inputs

- `SOURCE`: Chinese subtitle file, one subtitle per line, or an SRT file.
- `BRIEF`: short film background (characters, genre, register). If the user gave
  none, ask once; otherwise don't stop to ask anything.
- `OUT_DIR`: a working folder next to SOURCE, e.g. `<source-name>-en/`.

If SOURCE is SRT: write the text of each entry to `OUT_DIR/source.txt`, one entry per
line (join an entry's lines with a space), translate that file, then rebuild
`OUT_DIR/result_en.srt` with the original numbers and timecodes copied byte-for-byte.

### baoyu-translate preferences

baoyu-translate blocks on a first-time setup when it finds no EXTEND.md. If none
exists at `.baoyu-skills/baoyu-translate/EXTEND.md` in the current project (or the
user-level paths that skill lists), copy `<skill-dir>/assets/EXTEND.md` to the
project path. Don't overwrite an existing one.

## Hard rules (from srt-translator + alterlab-cdm-subtitle-loc)

1. **Structure is frozen.** Output has exactly as many lines as the source text;
   line N translates line N. Never merge, split or reorder entries.
2. One subtitle ≤ 84 characters (2 × 42). Aim for ≤ 42 so it fits on one line.
3. Reading speed ≤ 17 CPS. Without timecodes the checker estimates it, so English
   should be about as short as the Chinese is quick.
4. Plain ASCII punctuation: no em/en dashes, no `--`, no curly quotes.
5. Same Chinese term → same English term every time, unless a character is
   deliberately varying it.

## Steps

### 1. Analyse and build the glossary — `baoyu-translate` (refined mode)

Read `<skills>/baoyu-translate/SKILL.md` and its `references/refined-workflow.md`.
Skip its chunking script for inputs under 4000 words, and skip the image pass when
there are no images. Write:

- `OUT_DIR/01-analysis.md`: who speaks each line where it can be inferred,
  register, dialect and slang, jokes and teasing, onomatopoeia, numbers/countdowns.
- `OUT_DIR/glossary.md` (markdown table `| from | to | note |`): recurring terms,
  nicknames, insults and objects, with one chosen rendering each.
- `OUT_DIR/terms.json`: the glossary as `{"中文词": ["english rendering", ...]}` for
  the checker (list the chosen rendering first; add close variants it should accept).
- `OUT_DIR/02-prompt.md`: the assembled brief (BRIEF + analysis + glossary + the
  hard rules above + the core rules of `<skills>/subtitle-translation/SKILL.md`).

### 2. Draft — `subtitle-translation` + `srt-translator`

Translate following `02-prompt.md` into `OUT_DIR/03-draft.txt`. From
`subtitle-translation`: spoken naturalness over literal structure, short lines, keep
jokes and emotion. From `srt-translator`: localize rather than translate word for
word; keep the structure.

### 3. Measure the draft — bundled checker

```bash
python3 <skill-dir>/scripts/subtitle_check.py SOURCE_TXT OUT_DIR/03-draft.txt --terms OUT_DIR/terms.json > OUT_DIR/03-draft-check.md
```

`SOURCE_TXT` is SOURCE, or `OUT_DIR/source.txt` for SRT input.

### 4. Critique — `baoyu-translate` review + `humanizer` + `alterlab-cdm-subtitle-loc`

Write `OUT_DIR/04-critique.md` (diagnosis only, no rewriting yet), covering:

- accuracy against the Chinese (baoyu-translate critique checklist),
- translationese and AI tells from `<skills>/humanizer/SKILL.md`. Apply the patterns
  that fit dialogue (stock AI words, staged openers, inflated wording, dashes,
  over-tidy grammar, filler); ignore prose-only ones (bold labels, headings),
- subtitle craft from `<skills>/alterlab-cdm-subtitle-loc/SKILL.md`: line length,
  reading speed, character voice consistency, grammatical units,
- every hard or soft item in `03-draft-check.md`.

Shortening must not drop meaning or tone: check each cut line against the Chinese
(for example, a 怎么 question should stay a question).

### 5. Revise and polish

Apply the critique → `OUT_DIR/05-revision.txt`, then a read-aloud polish →
`OUT_DIR/result_en.txt` (and `result_en.srt` for SRT input).

### 6. Verify before claiming done — `verification-before-completion`

Follow `<skills>/verification-before-completion/SKILL.md`:

```bash
python3 <skill-dir>/scripts/subtitle_check.py SOURCE_TXT OUT_DIR/result_en.txt --terms OUT_DIR/terms.json > OUT_DIR/check_report.md; echo "exit=$?"
```

Exit code must be 0 (no hard issues). If not, fix and re-run. Report what the
checker printed, including any soft notes you kept and why. Don't say "done"
without this fresh output.
