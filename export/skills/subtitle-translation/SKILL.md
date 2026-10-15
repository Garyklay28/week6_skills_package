---
name: subtitle-translation
description: Use this for subtitle and caption translation. Optimizes for spoken naturalness, brevity, timing-friendly phrasing, and readability on screen rather than literal line-by-line transfer.
---

# Subtitle Translation

Translate speech into subtitles that read naturally on screen.

## Scope Boundary

- Use this for spoken dialogue, captions, and subtitle-style lines where speed and readability matter.
- For general prose that is not meant to be read on screen in real time, use `general-translation`.

## Use Cases

- subtitles
- captions
- transcript cleanup
- short spoken lines
- video translation

## Core Rules

- Preserve meaning, tone, and speaker intent.
- Prefer spoken naturalness over literal structure.
- Keep lines brief and easy to scan.
- Remove wording that feels too formal for speech unless the speaker is formal.
- Keep jokes, emotion, and rhythm when possible without over-expanding.
- If a literal translation is accurate but sounds written, shorten and reframe it into natural spoken target-language rhythm.

## Inputs To Infer

- source language
- target language
- audience
- tone
- subtitle/caption constraints

## Failure Modes To Prevent

- lines that are too long
- stiff written-language phrasing
- lost emotional tone
- overexplained speech
- formal pronoun or verb choices that break spoken dialogue feel

## Wording Guidance

- Prefer spoken verbs and particles when they fit the speaker and audience.
- In reactive or emotional dialogue, favor quick rhythm over grammatically tidy phrasing.
- Keep subtitle lines moving. A line can be slightly rougher if it sounds more like real speech and remains clear.

Prefer:

- `chat kamu`
- `marah sama aku`
- `aku udah nelepon kamu`
- `emang aku harus ngapain?`

Over:

- `mengirim pesan kepadamu`
- `marah kepadaku`
- `aku memang meneleponmu`
- `aku harus melakukan apa`

## Final Check

- Would this be easy to read quickly?
- Does it sound like something a person would actually say?
- Was important tone preserved?
