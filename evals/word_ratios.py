"""Watch-word discrimination ratios: AI corpus vs human corpora.

    python evals/word_ratios.py

Counts the §12 watch words in our AI-side corpus (evals/corpus + corpus2) and
compares per-100k rates against the human baselines frozen in
results/oanc-sweep.json (11.49M words) and results/masc-sweep.json (379k
words). Writes results/word-ratios.json and prints a summary table.
"""

import json
import re
from pathlib import Path

WATCH = ["delve", "tapestry", "garner", "seamless", "seamlessly", "leveraging",
         "leverage", "unlock", "unlocking", "showcase", "showcases",
         "meticulous", "meticulously", "interplay", "intricate", "bolster",
         "navigate", "underscore", "underscores", "testament", "enduring",
         "quietly", "pivotal", "optimize", "optimizing", "vibrant", "realm",
         "align", "highlight", "robust", "enhance", "enhancing", "foster",
         "landscape", "crucial", "comprehensive", "seamlessly"]


def count(words, text):
    low = text.lower()
    hits = 0
    for w in words:
        hits += len(re.findall(rf"\b{re.escape(w)}\b", low))
    return hits


def main():
    root = Path(__file__).parent
    ai_texts = []
    for d in ("corpus", "corpus2"):
        for f in sorted((root / d).glob("*.md")):
            ai_texts.append(f.read_text(encoding="utf-8"))
    ai_words = sum(len(t.split()) for t in ai_texts)

    oanc = json.loads((root / "results" / "oanc-sweep.json")
                      .read_text(encoding="utf-8"))
    masc = json.loads((root / "results" / "masc-sweep.json")
                      .read_text(encoding="utf-8"))

    rows = {}
    for w in WATCH:
        ai_hits = sum(count([w], t) for t in ai_texts)
        ai_rate = ai_hits / ai_words * 100000
        h_oanc = oanc["watch_words"].get(w, {}).get("per_100k", 0.0)
        h_masc = masc["watch_words"].get(w, {}).get("per_100k", 0.0)
        h_rate = (oanc["watch_words"].get(w, {}).get("hits", 0)
                  + masc["watch_words"].get(w, {}).get("hits", 0)) \
            / (oanc["words_total"] + masc["words_total"]) * 100000
        ratio = round(ai_rate / h_rate, 1) if h_rate > 0 else None
        rows[w] = {"ai_per_100k": round(ai_rate, 2), "ai_hits": ai_hits,
                   "human_per_100k": round(h_rate, 3),
                   "oanc_per_100k": h_oanc, "masc_per_100k": h_masc,
                   "ratio": ratio}
    result = {
        "ai_files": len(ai_texts), "ai_words": ai_words,
        "human_words": oanc["words_total"] + masc["words_total"],
        "words": rows,
    }
    out = root / "results" / "word-ratios.json"
    out.write_text(json.dumps(result, indent=1), encoding="utf-8")
    print(f"AI: {len(ai_texts)} files, {ai_words} words; "
          f"human: {result['human_words']:,} words")
    print(f"{'word':<14}{'AI/100k':>9}{'human/100k':>12}{'ratio':>8}")
    for w, v in sorted(rows.items(), key=lambda x: -(x[1]["ratio"] or 0)):
        r = v["ratio"] if v["ratio"] is not None else "n/a"
        print(f"{w:<14}{v['ai_per_100k']:>9}{v['human_per_100k']:>12}{r:>8}")


if __name__ == "__main__":
    main()
