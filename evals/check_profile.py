"""Voice-profile fixture check: facts stay out, claims stay in.

    python evals/check_profile.py --source SOURCE --rewrite REWRITE --profile PROFILE

Two mechanical checks on a profile-driven rewrite (the style judgment itself
stays human, per results/profile-fixture.md):

1. Claims preserved: every number and dollar amount in the source must appear
   in the rewrite. Missing claim = fail.
2. Exemplar leakage: the profile's exemplar passages (blockquote lines) are a
   different writer's content. Any run of 3+ distinctive words (length > 4,
   not stopwords) copied from one exemplar into the rewrite = fail.
"""

import re
import sys
from pathlib import Path

STOP = set("the a an and or but so of to in on for with at by from as is are "
           "was were be been it its this that these those we our you your they "
           "their there here what which who whom how when where not no yes if "
           "then than them us he she his her him has have had do does did will "
           "would can could should may might up out about into over after "
           "before under again very just".split())


def claims(source):
    return re.findall(r"[\$]?\d[\d,.]*\s*%?", source)


def leak(rewrite_words, exemplars):
    hits = []
    for i, ex in enumerate(exemplars):
        tokens = [w.lower() for w in re.findall(r"[A-Za-z']+", ex)
                  if len(w) > 4 and w.lower() not in STOP]
        run = best = 0
        for w in rewrite_words:
            if w.lower() in tokens:
                run += 1
                best = max(best, run)
            else:
                run = 0
        if best >= 3:
            hits.append((i, best))
    return hits


def main():
    args = dict(zip(sys.argv[1::2], sys.argv[2::2]))
    source = Path(args["--source"]).read_text(encoding="utf-8")
    rewrite = Path(args["--rewrite"]).read_text(encoding="utf-8")
    profile = Path(args["--profile"]).read_text(encoding="utf-8")

    ok = True
    rw = re.sub(r"##? .*", "", rewrite)  # ignore headings
    for c in claims(source):
        if c.strip() not in rewrite:
            print(f"FAIL missing claim: {c!r}")
            ok = False
    exemplars = [ln.lstrip("> ").strip() for ln in profile.splitlines()
                 if ln.startswith(">") and len(ln.strip()) > 5]
    hits = leak(re.findall(r"[A-Za-z']+", rw), exemplars)
    for i, best in hits:
        print(f"FAIL exemplar {i} leakage: {best}-word run copied")
        ok = False
    if not exemplars:
        print("note: no exemplar blockquotes found in profile")
    print("PASS" if ok else "FAIL")


if __name__ == "__main__":
    main()
