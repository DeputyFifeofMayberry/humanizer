# Profile eval fixture — 2026-10-11

Closes the 3.4.0 evidence gap: does a saved voice profile change the rewrite's
style, without leaking the profile's content or dropping the source's claims?

## The case

- Source: `evals/corpus/ai_email_vendor.md` (the Q3 vendor-consolidation email)
- Profile: `references/profiles/example-site-updates.md` (construction PM
  writing to crew and subs — short sentences joined by "so", specifics named,
  contractions, ends on the ask; exemplars are a subcontractor number, a steel
  delivery, and an RFI deadline)
- Rewrite under profile: `evals/rewrite/profile_email_v360.md`
- Command:

```
python evals/check_profile.py --source evals/corpus/ai_email_vendor.md \
  --rewrite evals/rewrite/profile_email_v360.md \
  --profile references/profiles/example-site-updates.md
```

## Checks

1. **Claims preserved (mechanical, committed as `check_profile.py`).** Every
   number and dollar amount in the source appears in the rewrite: 23%, 15%,
   $400k, twelve → four, November 1st, Thursday. Run it — PASS.
2. **Exemplar leakage (mechanical).** No run of 3+ distinctive words copied
   from the profile's exemplar passages (subcontractor numbers, steel decking,
   RFI) appears in the rewrite. Run it — PASS.
3. **Style shift (human, this fixture's worked example).** The rewrite reads
   in the profile's voice — "Phase one wrapped up", "so costs are down",
   "Need you at Thursday's standup" — rather than the source's voice
   ("I'm thrilled to announce", "significant milestone"). Verified by
   inspection against the profile's style summary and voice bands; automated
   style scoring would need a judged corpus and stays out of scope.

## What this fixture proves

Profile mechanics work: style transfers, content does not, source claims
survive. It does not prove a real writer's profile (built from their samples)
behaves identically — that needs a real profile and its owner's judgment,
which is exactly what the README's replacement flow sets up.
