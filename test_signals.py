#!/usr/bin/env python3
"""
Plain assertions for the pure, deterministic parts of this service.

    python test_signals.py

Everything in scoring.py, stylometry.py and lexical.py takes a string in and
a float out — no server, no model download, no network. These run in
milliseconds and are what should catch a regression when weights or
thresholds get tuned, instead of only finding out via a manual curl.

Not exhaustive — this is the handful of edge cases worth having an assertion
for, not full coverage: empty input, single-sentence input (the stdev edge
case stylometry.py's own docstring calls out), and the exact label-boundary
scores where the README's ranges meet the code's `<=`/`>=` comparisons.
"""

import lexical
import scoring
import stylometry

PASS = 0
FAIL = 0


def check(name: str, condition: bool) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"[PASS] {name}")
    else:
        FAIL += 1
        print(f"[FAIL] {name}")


# ── stylometry.py ─────────────────────────────────────────────────────────────

check(
    "sentence_length_spread: empty text returns 0.0, not an exception",
    stylometry.sentence_length_spread("") == 0.0,
)

check(
    "sentence_length_spread: one sentence returns 0.0 (stdev needs 2+ values)",
    stylometry.sentence_length_spread("Just one sentence here.") == 0.0,
)

check(
    "type_token_ratio: empty text returns 0.0",
    stylometry.type_token_ratio("") == 0.0,
)

check(
    "type_token_ratio: no repeated words returns 1.0",
    stylometry.type_token_ratio("one two three four") == 1.0,
)

check(
    "punctuation_density: text with no punctuation returns 0.0",
    stylometry.punctuation_density("no punctuation marks at all here") == 0.0,
)

check(
    "style_signal: always lands in 0.0-1.0",
    0.0 <= stylometry.style_signal("Some ordinary text; with a semicolon.") <= 1.0,
)

check(
    "style_signal: empty text doesn't raise and stays in range",
    0.0 <= stylometry.style_signal("") <= 1.0,
)


# ── lexical.py ────────────────────────────────────────────────────────────────

check(
    "lexical_signal: empty text returns the neutral midpoint, not an exception",
    lexical.lexical_signal("") == 0.5,
)

check(
    "lexical_signal: always lands in 0.0-1.0",
    0.0 <= lexical.lexical_signal("Some unremarkable sentence about nothing.") <= 1.0,
)


# ── scoring.py ────────────────────────────────────────────────────────────────

check(
    "combine_signals: three signals at 1.0 combine to 1.0",
    scoring.combine_signals(1.0, 1.0, 1.0) == 1.0,
)

check(
    "combine_signals: three signals at 0.0 combine to 0.0",
    scoring.combine_signals(0.0, 0.0, 0.0) == 0.0,
)

check(
    "combine_signals: two-signal call (no lexical_score) still returns 0.0-1.0",
    0.0 <= scoring.combine_signals(0.5, 0.5) <= 1.0,
)

check(
    "score_to_label: exactly at HUMAN_THRESHOLD is 'human' (the <= boundary)",
    scoring.score_to_label(0.35)[0] == "human",
)

check(
    "score_to_label: just above HUMAN_THRESHOLD is 'unsure'",
    scoring.score_to_label(0.36)[0] == "unsure",
)

check(
    "score_to_label: exactly at AI_THRESHOLD is 'ai' (the >= boundary)",
    scoring.score_to_label(0.65)[0] == "ai",
)

check(
    "score_to_label: just below AI_THRESHOLD is 'unsure'",
    scoring.score_to_label(0.64)[0] == "unsure",
)

check(
    "score_to_label: all three guesses are reachable",
    {scoring.score_to_label(s)[0] for s in (0.0, 0.5, 1.0)} == {"human", "unsure", "ai"},
)


print(f"\n{PASS} passed, {FAIL} failed")
if FAIL:
    raise SystemExit(1)
