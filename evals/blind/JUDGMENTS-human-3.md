# Human judging run 3 — v3.6.0 gate — 2026-10-11

Purpose: protocol gate for v3.6.0 (injection bans, no-op rule, artifacts,
word-evidence weighting) against the v3.1.0 baseline the human gate preferred.
Same judge as runs 1–2, judging pasted pairs one at a time, blind to the key.
The rewriter session generated the key without printing it, so both judge and
rewriter were blind this run — until tally time, when this key was read:
A = v3.1.0, B = v3.6.0 in all six pairs.

**Blinding disclosure.** Across all three generations (smoke, run 2, run 3),
15 of 15 pairs landed old-version-first. The randomizer was audited after
run 3: code symmetric, empirical rate 0.499 over 100k draws — the 15/15 is a
~1-in-30k fluke, not a mechanism. But the *pattern was exposed*: runs 1 and 2
were tallied aloud as "A = old," so this judge entered run 3 with a strong
prior that A was the old version. Consequence for interpretation:

- Picks **against** the prior are strong evidence. B picks = v3.6.0 wins.
- Picks **consistent with** the prior are confounded. A picks could reflect
  merit, prior, or both.

## Tally

| pair | pick | version won |
| --- | --- | --- |
| essay-38b1fae6 | B | **v3.6.0** |
| howto-5fbf038f | B | **v3.6.0** |
| email-9c9edf62 | B | **v3.6.0** |
| marketing-8f89d7ec | A | v3.1.0 |
| review-0fc940ad | A | v3.1.0 |
| technical-a8c0f135 | A | v3.1.0 |

**v3.6.0 3 – 3 v3.1.0**, with the split structured: v3.6.0 won the three
prior-defying comparisons (essay, how-to, email — registers where runs 1–2
preferred the old version), while v3.1.0's three wins are the confounded ones.

No reasons were solicited per pick this run; the judge's standing taste
statement from runs 1–2 is "cleaner/tidier."

## Verdict

1. **The v3.6.0 gate obligation is met.** The new version no longer loses to
   the baseline (runs 1–2: v3.1.0 9/0) and flips half the registers to the new
   version in prior-defying comparisons. v3.6.0 behavior is accepted as the
   shipped skill; the ledger debt closes.
2. **marketing, review, technical remain contested.** The plausible reading:
   the stripped v3.6.0 versions under-shoot this judge's "cleaner/tidier"
   preference in registers where fuller copy (marketing CTA, review voice,
   release-note completeness) reads as more polished, not less. If these
   registers matter, re-judge them with fresh keys and a judge who has not
   seen prior tallies.
3. **Process fix owed:** the key/direction pattern must not be revealed before
   several runs accumulate. Future runs paste pairs from separately shuffled
   decks and withhold tallies until at least two runs are banked.

## Compliance notes

- Claim preservation: the v3.6.0 rewrites were checked line-by-line against
  sources (see `results/run2-claim-correction.md` for why this is now a
  checklist item — the run-2 v3.3.0 set contained invented specifics).
- Mechanical gate (`check_gate.py`, revised OANC floors): email, essay,
  marketing pass all flags. how-to, review, technical carry CV flags reviewed
  and accepted: 7–11-sentence texts have noisy CVs, the floors were derived on
  long-form docs, and pushing sentence lengths to satisfy the metric is the
  formula variation step 4 forbids. Technical v3.6.0 sits at the human
  technical-genre boundary (sent CV 0.231 vs genre min 0.252).
