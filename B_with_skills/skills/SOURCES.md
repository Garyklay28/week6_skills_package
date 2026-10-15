# Skill sources

Each folder is copied unchanged from its upstream repository at the commit below (fetched 2026-10-15), with that repository's `LICENSE` placed next to it. `subtitle-zh-en-pipeline` is the only skill written for this package.

| Skill | Role in the pipeline | Upstream | Path in upstream | Commit | License |
|---|---|---|---|---|---|
| `baoyu-translate` | Analysis → glossary → draft → critique → revision → polish (refined mode) | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | [`skills/baoyu-translate`](https://github.com/JimLiu/baoyu-skills/tree/1567581c26ec29f4216c6e6835415bf30343b0e3/skills/baoyu-translate) | `1567581` | MIT |
| `subtitle-translation` | Spoken naturalness, brevity, on-screen readability | [srmdn/open-writing](https://github.com/srmdn/open-writing) | [`skills/subtitle-translation`](https://github.com/srmdn/open-writing/tree/b410865d808bc2335ef40b613ca869917a963e17/skills/subtitle-translation) | `b410865` | Apache-2.0 |
| `srt-translator` | Keep entry count/timing frozen, localize instead of word-for-word | [nicepkg/ai-workflow](https://github.com/nicepkg/ai-workflow) | [`workflows/video-creator-workflow/.claude/skills/srt-translator`](https://github.com/nicepkg/ai-workflow/tree/d167b41af7f013d3d3c35dca87a6cc72817721d2/workflows/video-creator-workflow/.claude/skills/srt-translator) | `d167b41` | MIT |
| `alterlab-cdm-subtitle-loc` | Subtitle standards: 42 chars/line, 2 lines, 17 CPS, consistent voice | [AlterLab-IEU/AlterLab-FC-Skills](https://github.com/AlterLab-IEU/AlterLab-FC-Skills) | [`skills/cdm/alterlab-cdm-subtitle-loc`](https://github.com/AlterLab-IEU/AlterLab-FC-Skills/tree/9559c97a6b6fc90c0fbe5a20b7718716f7aee677/skills/cdm/alterlab-cdm-subtitle-loc) | `9559c97` | MIT |
| `humanizer` | Remove AI writing tells (based on Wikipedia "Signs of AI writing") | [blader/humanizer](https://github.com/blader/humanizer) | [`SKILL.md`](https://github.com/blader/humanizer/blob/225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8/SKILL.md) | `225a6f3` | MIT |
| `verification-before-completion` | No "done" without fresh checker output | [obra/superpowers](https://github.com/obra/superpowers) | [`skills/verification-before-completion`](https://github.com/obra/superpowers/tree/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/verification-before-completion) | `bb92a77` | MIT |
| `subtitle-zh-en-pipeline` | Orchestrator: which skill runs at which step | this repo | `B_with_skills/skills/subtitle-zh-en-pipeline` | — | MIT |

`B_with_skills/scripts/subtitle_check.py` and `eval_terms.json` were also written for this package.
