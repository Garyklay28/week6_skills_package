# 04 Critique of `03-draft.txt` (diagnosis only)

Inputs: `03-draft.txt`, `03-draft-check.md` (PASS, 0 hard, 3 soft), `01-analysis.md`,
`glossary.md`. Checklists: baoyu-translate refined-workflow Step 4, humanizer pattern
list (dialogue-relevant items only), alterlab-cdm-subtitle-loc subtitle craft.

## Accuracy (baoyu-translate 4.1)

- Structure: 97/97 lines, line-aligned, no merges or splits. OK.
- Glossary terms (老头/火车/隧道/胆小鬼/护身符): all consistent per checker. OK.
- 14 他刚刚就在这啊: "He was right here just now." is accurate but long; "just now" can go into "just" ("He was just here!").
- 15 他跟我说什么火车马上要来了: draft "a train coming soon" weakens 马上 (any minute) and drops the dismissive 什么 ("something about some train"). Fix both.
- 16 让咱赶紧走: "He said we should leave right away" is accurate but reported-speech heavy; 让 = told us to.
- 18 这儿哪有火车: rhetorical denial; "There's no train around here" OK in meaning, but over length.
- 24 不信？走去看看呗: 呗 is a casual "let's just go see", draft "Let's go take a look" is fine but long.
- 50 反正你也不敢进: keep the "anyway / not like you'd dare" taunt logic when shortening.
- 69 至于吗: draft "Is it really that serious?" is a literal calque of the rhetorical question; the speaker means "relax, it was a joke".
- 72 下次赢了就是你赢了: draft "If you win next time, then you're the winner" is accurate but reads like a rule sheet. Meaning: B "generously" lets the next round decide everything.
- 83 你还敢自己出来: draft "You actually dare to come out by yourself?" is a word-for-word calque; the line is mock-outrage at the hider showing himself.
- 85 哎嘿: draft "Hehe!" duplicates 42 嘿嘿 ("Hehe."). Different sound in the source (a cheeky dodge), so it should read differently.
- 89 你也有今天呀: draft "Look who's in trouble now!" drifts from the analysis plan "Look who's stuck now!", which ties directly to 62/66 (A stuck earlier) and to the climax. Use the planned line.
- 92 拉我 哎: "Pull me up... hey!" ellipsis suggests trailing off; the source is two beats (pull me / hey!). Two exclamations read better.

## Native Voice (baoyu-translate 4.2 + humanizer)

Humanizer patterns that apply to dialogue:

- **Inflated wording (§12/§13 spirit)**: 33 "experience it too" (体验一下 calque; no kid says "experience it"). -> "come up here too".
- **Over-tidy grammar / filler (humanizer: over-tidy, stacked words)**:
  - 6 "make you go stupid or something" (filler "or something", 57 chars) -> "Did getting caught fry your brain?"
  - 70 "This time, I'm the one who won." (cleft construction, stiff) -> "So this round, I win."
  - 71 "But I'm willing to go easy on you." (willing to = written register) -> "But I'll cut you some slack."
  - 72 if/then rule-sheet phrasing (see Accuracy).
  - 53 "What is there to be scared of?" (uncontracted; checker soft note) -> "What's to be scared of?"
  - 64 "Don't try to scare me." (padding "try to") -> "Don't scare me."
  - 66 "Hurry up and pull me up." (up/up repetition) -> "Pull me up, quick!"
- **Translationese "Go and ..."**: 57 "Go and pick it up yourself", 59 "Go and get it back for me", 73 "Okay, go and hide": the "go and" pattern is a calque of 去...去 and sounds British/written for US-style kid dialogue. -> "Go get it yourself." / "Go get it back!" / "Okay, go hide."
- **Repeated phrasing by rule**: 34 and 36 both "Just try it." after 33 already says try. Source 试试嘛 / 你试试 differ (coaxing vs. pushing); vary.
- Dashes, curly quotes, semicolons, stock AI words: none. OK.
- Ignored as prose-only: bold labels, headings, chat residue (not present in subtitles).

## Subtitle craft (alterlab-cdm-subtitle-loc)

- **Line length**: 9 lines over 42 chars (6, 10, 15, 33, 48, 49, 69, 72, 75). All but 48 can be brought to one line without loss. 48 is a two-part taunt (insult + condition); acceptable as a 2-line subtitle if it stays within reading speed.
- **Reading speed**: 49 of 97 lines over the estimated 17 CPS. The worst offenders are short Chinese lines carrying full English sentences:
  - 16 (35 chars vs ~18 budget), 25 (30 vs 17), 79 (32 vs 18), 82 (33 vs 18), 83 (42 vs 26), 84 (34 vs 22), 90 (35 vs 26), 95 (41 vs 30), 69 (46 vs 34), 72 (45 vs 34), 22 (42 vs 30), 23 (37 vs 26).
  - Strategy (condensation): drop subjects and fillers kids drop anyway ("He said we should" -> "Told us to"), use contractions ("Where'd"), cut tags the picture already shows ("in your hand" can stay only if it fits).
  - Some 1-3 character overages on 1-second lines (e.g. 26 "Where's the train?" 18/17, 37 "There's the old man!") are acceptable: the estimate assumes 4.5 hanzi/s and a 1 s floor, while real kid speech with pauses runs longer. Don't mangle clear lines to shave 1-3 chars.
- **Glossary rendering too long**: 早就没火车来了 -> "No trains have come here in ages" (33 chars) blows the 26-char budget on both 23 and 28. Change glossary entry to "No trains for years" and apply to both lines so the repetition still echoes.
- **Character voice consistency**: B (skeptic) should sound cocky and clipped ("Quit lying." "OK?" "Relax."); A should sound anxious and urgent. Draft B lines 70-72 sound adult and polite; fix.
- **Grammatical units**: 32/33 split ("If you ask me, / you should...") matches the source split; keep lowercase continuation. 78/79 likewise.

## Checker items from `03-draft-check.md`

- Hard: none.
- Soft: over 42 chars [6, 10, 15, 33, 48, 49, 69, 72, 75] -> addressed above.
- Soft: CPS > 17 on 49 lines -> condense per above; target well under half of that.
- Soft: uncontracted "what is" (53) -> contract.
- Terms: consistent; keep.

## Summary

0 critical accuracy errors. Main problems: (1) reading speed / length, about half the
lines are too long for their screen time; (2) stiff or calqued phrasing (33, 69, 70-72,
83, the "go and" lines); (3) small consistency and voice slips (23/28 glossary line too
long, 85 duplicating 42, 89 drifting from plan, 34/36 duplicate).
