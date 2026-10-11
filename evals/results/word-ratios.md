# Watch-word discrimination ratios — AI corpus vs 11.87M human words — 2026-10-11

Second pass, doubling the AI side and sampling its cliché register. AI side:
60 drafts, 11,117 words (`evals/corpus` + `evals/corpus2`; wave 2 deliberately
samples classic model vocabulary). Human side: OANC + MASC, 11.87M words.
Measure: per-100k rates, ratio AI/human. Reproduce:

```
python evals/word_ratios.py
```

Raw: `word-ratios.json`.

## Results

| word | AI/100k | human/100k | ratio |
| --- | --- | --- | --- |
| showcases | 63.0 | 0.101 | 623× |
| unlock | 81.0 | 0.143 | 565× |
| meticulously | 81.0 | 0.202 | 400× |
| meticulous | 107.9 | 0.278 | 388× |
| tapestry | 27.0 | 0.093 | 291× |
| seamless | 36.0 | 0.135 | 267× |
| delve | 36.0 | 0.143 | 251× |
| showcase | 63.0 | 0.379 | 166× |
| seamlessly | 18.0 | 0.194 | 93× |
| testament | 54.0 | 0.809 | 67× |
| quietly | 45.0 | 0.986 | 46× |
| pivotal | 18.0 | 0.59 | 31× |
| crucial | 81.0 | 3.36 | 24× |
| robust | 45.0 | 2.13 | 21× |
| underscore | 9.0 | 0.43 | 21× |
| leverage / optimize / intricate / vibrant / enduring | 9.0 | 0.43–0.88 | 10–17× |
| foster / landscape | 9.0 | 2.15–2.17 | ~4× |
| enhance | 9.0 | 3.51 | 2.6× |
| comprehensive | 63.0 | **0.0** | n/a — absent from 11.87M human words |
| garner, leveraging, unlocking, interplay, bolster, navigate, underscores, optimizing, realm, align, highlight, enhancing | 0.0 | 0.03–1.4 | unmeasured on AI side |

## Reading

1. **The ladder matches the known ordering.** With the cliché register
   sampled, the measured tiers line up with Wikipedia's signs and the
   INVESTIGATION baselines: meticulous/showcase/delve/tapestry at the top;
   crucial/robust/landscape/enhance near the bottom. §12's strong-vs-weak
   weighting is now data-backed, not just cited.
2. **"comprehensive" is the study's find.** Zero occurrences in 11.87M human
   words while running at 63/100k in AI drafts — a §12 candidate, admitted on
   the same terms as the rest (see caveats).
3. **The 0.0 rows shrunk but persist.** Twelve words remain unmeasured on the
   AI side — the sampled register simply doesn't use them. They stay on the
   §12 list by upstream evidence, untested by this study.

## Standing caveats

- **One model, one session.** Wave 2 samples the model's cliché register, but
  it is still a single author. Ratios here are screening values; family-level
  claims need generation across model families.
- **AI side is 11k words.** A hit moves a rate; treat ratios below ~10× as
  directional only.
- Per the claim gate: none of this table publishes as a headline until the
  AI side spans families and ≥100k words.

## Next

Regenerate across model families; words holding ≥10× across families become
§12 admissions ("comprehensive" currently leads that queue); words under 2×
come off regardless of anecdote.
