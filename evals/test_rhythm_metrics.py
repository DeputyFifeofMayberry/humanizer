"""Assert-based self-check for rhythm_metrics. Run: python evals/test_rhythm_metrics.py"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from rhythm_metrics import measure

METRONOMIC = """\
Teams need alignment. Teams need focus. Teams need ownership. Alignment drives outcomes.
Focus drives outcomes. Ownership drives outcomes. These three principles matter greatly.
Leaders must communicate clearly. Leaders must listen actively. Leaders must adapt quickly.
Clear communication matters greatly. Active listening matters greatly. Quick adaptation matters.
"""

VARIED = """\
The migration failed on a Tuesday. Not because of the schema, which had been tested to
destruction over three weeks of dry runs, but because nobody had checked whether the
reporting warehouse would survive the cutover window. It didn't.

We rolled back by 6 a.m. Cost: one missed SLA, some bad feeling, and a mandate to write
this down somewhere. So here it is: check the warehouse first. The schema can wait.
"""

m1 = measure(METRONOMIC)
m2 = measure(VARIED)

# Metronomic text: anaphora runs detected, high uniformity (low CV), short uniform sentences
assert m1["anaphora_runs"] >= 1, f"anaphora missed: {m1}"
assert m1["sentence_len_cv"] < m2["sentence_len_cv"], "CV should be lower for uniform text"
assert m1["triads"] >= 0

# Varied text: should look more human on the uniformity proxies
assert m2["para_word_cv"] > 0, "paragraph variation should be nonzero"

# Punchy closer detection: final paragraph tightens into a short last line
assert m2["punchy_closers"] >= 1, f"closer missed: {m2}"

# Contractions counted in the human sample
assert m2["contraction_rate"] >= 0.1, f"contractions missed: {m2}"

# Edge cases don't crash
assert measure("")["sentences"] == 0
assert measure("```python\ncode with. periods\n```")["sentences"] == 0

print("test_rhythm_metrics: all assertions passed")
