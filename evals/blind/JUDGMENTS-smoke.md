# Smoke judging run — 2026-10-10

**Contamination disclosure:** the rewriter and the judge were the same model in
the same session, and the judge knew the key. This run validates the pairing and
tally pipeline end to end. It is NOT evidence of improvement. Cross-family or
human judging per `evals/README.md` is still owed.

Method: quality-only, forced choice, confidence 1-5, one quoted reason.

| pair | pick | conf | reason (quoted from pair) |
| --- | --- | --- | --- |
| essay-3f206ad7 | B | 4 | A ends "fundamentally human endeavor" (aphoristic closer, §13-style send-off); B ends on a concrete fact |
| howto-2b25593c | B | 5 | B has actual opinion ("Don't overbuy", "$100 router does most apartments") and uneven section lengths; A is tidy and faceless |
| email-94e6fab3 | B | 4 | A's "This happened because of your flexibility" is a floating tribute; B names what the flexibility did ("without service gaps") |

Tally vs key (see tally in results/): B = v3.3.0 in all three.
