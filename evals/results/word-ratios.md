# Watch-word discrimination ratios — AI corpus vs 11.87M human words — 2026-10-11

First pass at the humanist-style study. AI side: 42 drafts, 7,757 words
(`evals/corpus` + `evals/corpus2`, six registers). Human side: OANC + MASC,
11.87M words. Measure: per-100k rates, ratio AI/human. Reproduce:

```
python evals/word_ratios.py
```

Raw: `word-ratios.json`.

## Results

| word | AI/100k | human/100k | ratio |
| --- | --- | --- | --- |
| seamless | 51.6 | 0.135 | 382× |
| unlock | 38.7 | 0.143 | 270× |
| seamlessly | 12.9 | 0.194 | 66× |
| quietly | 51.6 | 0.986 | 52× |
| underscore | 12.9 | 0.43 | 30× |
| optimize | 12.9 | 0.565 | 23× |
| pivotal | 12.9 | 0.59 | 22× |
| vibrant | 12.9 | 0.632 | 20× |
| testament | 12.9 | 0.809 | 16× |
| crucial | 25.8 | 3.36 | 7.7× |
| robust | 12.9 | 2.13 | 6.0× |
| landscape | 12.9 | 2.17 | 5.9× |
| enhance | 12.9 | 3.50 | 3.7× |
| delve, tapestry, garner, showcase, meticulous, intricate, bolster, realm, align, foster, highlight, endure, leverage(-ing), unlocking, optimizing | 0.0 | 0.03–2.1 | 0 |

## What this says — and what it cannot say

**Says:** the §12 three-tier idea has data. Words split cleanly into strong
markers (≥16×: seamless, unlock, quietly, underscore, pivotal, vibrant,
testament), medium markers (4–8×: crucial, robust, landscape, enhance), and
everyday words. The §12 sentence added in 3.6.0 (delve/tapestry/garner as
near-machine-only, rest weighed lower) matches the measured ordering. One new
candidate surfaced: **"comprehensive"** — 25.8/100k in the AI drafts, zero in
11.87M human words. Flagged for §12/§16, pending the caveats below.

**Cannot say:** anything about models other than the one that wrote these
drafts. The 0.0 rows are the giveaway — delve, tapestry, and showcase score
zero because *this corpus's author* doesn't reach for them, not because
modern models don't. One author's idiolect is all over the AI side. The
high-ratio rows are the honest ones (words the author actually used still
measure 4–382× human rate); the zero rows are an authorship artifact until
the corpus is regenerated across several models.

**Numbers context:** AI side is 7,757 words — a rate on that is a coarse
estimate, not a publication-grade claim (a hit or two moves it a lot). Human
side is solid. Per the claim gate adopted from avoid-ai-writing, this table
stays internal until the AI side spans multiple models and ~10× the words.

## Next

Regenerate the AI corpus across 3+ model families, same registers; re-run.
Words holding a ratio ≥ 10× across families become §12 candidates; words
below 2× stay off the list regardless of anecdote.
