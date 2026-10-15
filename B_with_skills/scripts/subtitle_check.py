#!/usr/bin/env python3
"""Check a line-aligned English subtitle translation against its Chinese source.

Usage:
  python3 subtitle_check.py SOURCE.txt TRANSLATION.txt [--terms eval_terms.json] [--json]

Both files are plain text, one subtitle per line; line N of the translation
translates line N of the source. Exit code is 0 when every HARD check passes,
1 otherwise. SOFT checks are reported but never fail the run.

No timecodes exist in the source, so reading speed is an ESTIMATE: each
subtitle's duration is guessed from the Chinese line at 4.5 hanzi/second
(minimum 1.0 s), and English CPS is computed against that guess.
"""
import argparse
import json
import re
import sys
from pathlib import Path

MAX_LINE = 42          # Netflix English: 42 chars per displayed line
MAX_SUB = 2 * MAX_LINE  # two displayed lines per subtitle
MAX_CPS = 17           # adult reading speed (Netflix English)
ZH_RATE = 4.5          # assumed hanzi per second of Chinese speech
MIN_DUR = 1.0

CJK = re.compile(r"[㐀-鿿　-〿＀-￯]")
HANZI = re.compile(r"[㐀-鿿]")

# Typography that chat models add and subtitle styles avoid.
HARD_MARKERS = {
    "em/en dash": re.compile(r"[—–]"),
    "curly quotes": re.compile(r"[“”‘’]"),
}
# Stock "AI" vocabulary (from humanizer / Wikipedia "Signs of AI writing").
AI_WORDS = re.compile(
    r"\b(delve|indeed|moreover|furthermore|utili[sz]e|embark|testament|tapestry|"
    r"pivotal|crucial|vibrant|meticulous|seamless|realm|journey|unveil|"
    r"navigate|foster|whilst|perhaps)\b", re.I)
# Uncontracted forms read stiff in kids' dialogue.
UNCONTRACTED = re.compile(
    r"\b(do not|does not|did not|is not|are not|was not|were not|cannot|can not|"
    r"will not|would not|should not|have not|has not|I am|you are|we are|they are|"
    r"it is|that is|there is|let us|I will|you will|I have|what is|where is)\b", re.I)
CONTRACTION = re.compile(r"\b\w+'(s|t|re|ve|ll|d|m)\b", re.I)


def load_lines(path):
    text = Path(path).read_text(encoding="utf-8")
    return text.rstrip("\n").split("\n")


def check(source, translation, terms=None):
    src = load_lines(source)
    out = load_lines(translation)
    hard, soft, rows = [], [], []

    if len(src) != len(out):
        hard.append(f"line count {len(out)} != source {len(src)}")

    over_line, over_sub, cps_flags, cjk_left, empty = [], [], [], [], []
    for i, en in enumerate(out, 1):
        zh = src[i - 1] if i <= len(src) else ""
        en_s = en.strip()
        if not en_s:
            empty.append(i)
        if CJK.search(en_s):
            cjk_left.append(i)
        n = len(en_s)
        if n > MAX_SUB:
            over_sub.append(i)
        elif n > MAX_LINE:
            over_line.append(i)
        dur = max(MIN_DUR, len(HANZI.findall(zh)) / ZH_RATE)
        cps = n / dur
        if cps > MAX_CPS:
            cps_flags.append(i)
        rows.append({"n": i, "zh": zh, "en": en_s, "chars": n, "est_cps": round(cps, 1)})

    if empty:
        hard.append(f"empty lines: {empty}")
    if cjk_left:
        hard.append(f"untranslated CJK left on lines: {cjk_left}")
    if over_sub:
        hard.append(f"over {MAX_SUB} chars (won't fit 2 lines): {over_sub}")
    if over_line:
        soft.append(f"over {MAX_LINE} chars, needs a 2-line break: {over_line}")
    if cps_flags:
        soft.append(f"estimated CPS > {MAX_CPS}: {cps_flags}")

    joined = "\n".join(out)
    marker_counts = {}
    for name, rx in HARD_MARKERS.items():
        hits = [i for i, en in enumerate(out, 1) if rx.search(en)]
        marker_counts[name] = len(hits)
        if hits:
            hard.append(f"{name} on lines: {hits}")
    ai_words = AI_WORDS.findall(joined)
    if ai_words:
        soft.append(f"stock AI words: {sorted(set(w.lower() for w in ai_words))}")
    unc = UNCONTRACTED.findall(joined)
    con = CONTRACTION.findall(joined)
    if unc:
        soft.append(f"uncontracted forms ({len(unc)}): {sorted(set(u.lower() for u in unc))}")
    semis = joined.count(";")
    if semis:
        soft.append(f"semicolons: {semis}")

    term_report = {}
    if terms:
        for zh_term, variants in terms.items():
            lines = [i for i, zh in enumerate(src, 1) if zh_term in zh]
            used, missing = {}, []
            for i in lines:
                en = out[i - 1].lower() if i <= len(out) else ""
                hit = [v for v in variants if v.lower() in en]
                if hit:
                    used.setdefault(hit[0], []).append(i)
                else:
                    missing.append(i)
            term_report[zh_term] = {"lines": lines, "renderings": used, "unmatched": missing}
            if len(used) > 1:
                soft.append(f"term {zh_term} rendered {len(used)} ways: {used}")

    total_chars = sum(r["chars"] for r in rows)
    metrics = {
        "lines": len(out),
        "source_lines": len(src),
        "total_chars": total_chars,
        "avg_chars": round(total_chars / max(1, len(out)), 1),
        "max_chars": max((r["chars"] for r in rows), default=0),
        "lines_over_42": len(over_line) + len(over_sub),
        "est_cps_over_17": len(cps_flags),
        "dash_or_curly": sum(marker_counts.values()),
        "stock_ai_words": len(ai_words),
        "uncontracted": len(unc),
        "contractions": len(con),
        "semicolons": semis,
        "terms_inconsistent": sum(1 for t in term_report.values() if len(t["renderings"]) > 1),
        "hard_fail": len(hard),
    }
    return {"ok": not hard, "hard": hard, "soft": soft, "metrics": metrics,
            "terms": term_report, "rows": rows}


def render(result, translation):
    m = result["metrics"]
    lines = [f"# Subtitle check: `{translation}`", "",
             f"**Result: {'PASS' if result['ok'] else 'FAIL'}** "
             f"({len(result['hard'])} hard issues, {len(result['soft'])} soft notes)", "",
             "## Metrics", "", "| metric | value |", "|---|---|"]
    lines += [f"| {k} | {v} |" for k, v in m.items()]
    lines += ["", "## Hard issues", ""] + ([f"- {h}" for h in result["hard"]] or ["- none"])
    lines += ["", "## Soft notes", ""] + ([f"- {s}" for s in result["soft"]] or ["- none"])
    if result["terms"]:
        lines += ["", "## Term consistency", "", "| term | source lines | renderings | unmatched |", "|---|---|---|---|"]
        for t, r in result["terms"].items():
            rend = "; ".join(f"{k}: {v}" for k, v in r["renderings"].items()) or "-"
            lines.append(f"| {t} | {r['lines']} | {rend} | {r['unmatched'] or '-'} |")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source")
    ap.add_argument("translation")
    ap.add_argument("--terms", help="JSON map of Chinese term -> list of accepted English renderings")
    ap.add_argument("--json", action="store_true", help="print JSON instead of markdown")
    a = ap.parse_args()
    terms = json.loads(Path(a.terms).read_text(encoding="utf-8")) if a.terms else None
    result = check(a.source, a.translation, terms)
    if a.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(render(result, a.translation), end="")
    sys.exit(0 if result["ok"] else 1)


if __name__ == "__main__":
    main()
