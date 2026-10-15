# A — Prompt only (no skills, no scripts)

This is the whole prompt given to a fresh agent. It had read access to the source file and nothing else from this repo.

---

Translate the Chinese subtitles in `input/字幕文件中文.txt` into English subtitles.

Film background: two kids play hide-and-seek near an abandoned railway tunnel. One says a mysterious old man came out of the tunnel and warned that a train is coming; the other doesn't believe it. At the end a train really comes. A coming-of-age / suspense short film, northern Chinese colloquial speech.

Requirements:
- The file has one subtitle per line (97 lines). Output exactly 97 lines; line N of your output translates line N of the source. Don't merge or split lines.
- Natural English that works as on-screen subtitles.
- Save the result as plain text to `A_no_skills/result_en.txt`.
