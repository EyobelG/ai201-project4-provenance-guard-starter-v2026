"""
Settings for Provenance Guard.

Everything you're likely to change lives here, at the top, on purpose.

You'll edit the thresholds in Milestone 5 and the rate limits in unit 8.
"""

import os
from pathlib import Path

ROOT = Path(__file__).parent


# ─── The service ─────────────────────────────────────────────────────────────

# `127.0.0.1` is loopback — only your own machine can reach it, which is what
# you want all through units 7 and 8. A host somewhere else has to accept
# traffic from outside the box, and that means `0.0.0.0`. Setting the env var
# is how you get it; the default keeps your local `curl` commands unchanged.
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", "5000"))

# Flask's debug mode gives anyone who can reach the service an interactive
# Python prompt inside your process. Fine on loopback, a gift to strangers
# anywhere else — so it turns itself off the moment HOST isn't loopback.
DEBUG = os.getenv("AI201_DEBUG", "1") == "1" and HOST in ("127.0.0.1", "localhost")


# ─── The local model ─────────────────────────────────────────────────────────
# Your first signal runs a language model ON YOUR OWN MACHINE. No account, no
# key, no card. It downloads about 550 MB the first time — do that before
# class, not during it.
#
# What it measures: how *predictable* your text is to a language model. Text a
# model finds easy to predict tends to be text a model wrote.
#
# The first call is the slow one — ten to twenty seconds while the model loads,
# longer on an older laptop. After that it stays in memory and a submission
# takes a second or two. That cost is part of what you're learning: this is
# what running a model inline in a request actually looks like.

DETECTOR_MODEL = os.getenv("AI201_DETECTOR_MODEL", "gpt2")

# Longer text gives a steadier reading but takes longer. 400 tokens is roughly
# 300 words, which is enough for the signal to mean something.
DETECTOR_MAX_TOKENS = 400

# Turning raw perplexity into a 0-1 score (detector.py::model_signal). The
# midpoint is the perplexity that scores 0.5; steepness controls how sharply
# the score moves either side of it. Move the midpoint once you've run real
# calibration text and seen where it actually lands — that's a scoring
# decision, so it lives here rather than buried in detector.py.
DETECTOR_PERPLEXITY_MIDPOINT = 45.0
DETECTOR_STEEPNESS = 1.6


# ─── Scoring (Milestone 4) ───────────────────────────────────────────────────
# How much each signal counts toward the combined score.
#
# ⚠️ These are placeholders. Milestone 4 asks you to write your combining rule
# down BEFORE you code it, and to put the numbers in your README. Whatever you
# decide, it goes here.

WEIGHT_MODEL_SIGNAL = 0.45
WEIGHT_STYLE_SIGNAL = 0.35

# Stretch: a third signal (lexical.py). Weighted lowest — it's the cheapest
# of the three to fool on purpose, so it earns the least trust by default.
# The three weights sum to 1.0.
WEIGHT_LEXICAL_SIGNAL = 0.20

# ─── Signal internals ────────────────────────────────────────────────────────
# Tuning knobs for the individual signals. Grouped here, not in each signal's
# module, so tuning after an attack run means editing one file, not four.

# stylometry.py::style_signal — how the three sub-measures combine.
STYLE_WEIGHT_SPREAD = 0.4       # sentence_length_spread
STYLE_WEIGHT_TTR = 0.3          # type_token_ratio
STYLE_WEIGHT_PUNCTUATION = 0.3  # punctuation_density

# stylometry.py — ceilings used to normalize raw measures onto 0-1 before
# they're combined. A coefficient of variation at or above this is treated as
# maximally human-like sentence variety; a punctuation density at or above
# this (marks per word) is treated as the human-like ceiling.
STYLE_SPREAD_CV_CEILING = 1.0
STYLE_PUNCTUATION_DENSITY_CEILING = 0.05

# lexical.py::lexical_signal — the "generic center" a text's distance is
# measured against, on function-word ratio and average word length.
LEXICAL_FWR_CENTER = 0.47
LEXICAL_AWL_CENTER = 4.5


# ─── Thresholds (Milestone 5) ────────────────────────────────────────────────
# Where one label becomes another. Scores run 0.0 (confidently human) to 1.0
# (confidently AI).
#
#   score < HUMAN_THRESHOLD          -> high-confidence human
#   between the two                  -> unsure
#   score > AI_THRESHOLD             -> high-confidence AI
#
# ⚠️ This is where your false-positive decision from Milestone 1 actually gets
# made. Widening the unsure band means fewer wrong accusations and more AI text
# getting through. There is no setting that avoids the trade — only settings
# that decide who pays for it.

HUMAN_THRESHOLD = 0.35
AI_THRESHOLD = 0.65

# ⚠️ One thing that catches people out in Milestone 5. A weighted average can
# only land between its two inputs — so while `style_signal` is still the stub
# returning 0.5, the combined score can never leave 0.25–0.75 no matter what
# the model signal says, and the human label needs a model score below 0.20 to
# be reachable at all.
#
# If a label you can't reach is the problem, the fix is upstream of the
# thresholds: a style signal that actually varies. `scoring.label_ranges()`
# prints the bands; the reachable range is a different question.


# ─── Rate limiting (UNIT 8) ──────────────────────────────────────────────────
# Off in unit 7. You turn it on and choose the numbers in unit 8, Milestone 1.
#
# Think about two people: a real writer submitting their own work a few times
# an hour, and a script sending a thousand variations to map your thresholds.
# Your README has to say why your numbers and not others.

RATE_LIMITING_ENABLED = os.getenv("AI201_RATE_LIMITS", "0") == "1"

RATE_LIMIT_PER_MINUTE = 10
RATE_LIMIT_PER_DAY = 200

# Flask-Limiter warns loudly without this. In-memory is right for one laptop
# and wrong for anything real — a restart forgets every count, and two copies
# of the service wouldn't share limits.
RATE_LIMIT_STORAGE = "memory://"


# ─── Request limits ──────────────────────────────────────────────────────────

# /submit rejects text longer than this with a 400, before any signal runs.
MAX_TEXT_CHARS = 20000


# ─── Paths ───────────────────────────────────────────────────────────────────

LOG_DIR = ROOT / "logs"
AUDIT_LOG = LOG_DIR / "audit.jsonl"
RESULTS_DIR = ROOT / "results"
