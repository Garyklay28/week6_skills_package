# B — Prompt with the skill package

This is the whole prompt given to a fresh agent. The film background and output requirements are word-for-word the same as A; the only difference is the instruction to use the skill package in `B_with_skills/`.

---

Translate the Chinese subtitles in `input/字幕文件中文.txt` into English subtitles.

Film background: two kids play hide-and-seek near an abandoned railway tunnel. One says a mysterious old man came out of the tunnel and warned that a train is coming; the other doesn't believe it. At the end a train really comes. A coming-of-age / suspense short film, northern Chinese colloquial speech.

Requirements:
- The file has one subtitle per line (97 lines). Output exactly 97 lines; line N of your output translates line N of the source. Don't merge or split lines.
- Natural English that works as on-screen subtitles.
- Save the result as plain text to `B_with_skills/result_en.txt`.

Use the skill package: start with `B_with_skills/skills/subtitle-zh-en-pipeline/SKILL.md` and follow it, reading the other skills in `B_with_skills/skills/` when it tells you to. Work from inside `B_with_skills/` (SOURCE = `../input/字幕文件中文.txt`, OUT_DIR = `work/`). baoyu-translate's preferences are in `B_with_skills/.baoyu-skills/baoyu-translate/EXTEND.md`.
