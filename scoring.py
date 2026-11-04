"""
Turning two numbers into one, and one number into something a person can read.
← YOU BUILD THIS IN MILESTONES 4 AND 5

Two functions live here, and both are stubs.

`combine_signals` is where your false-positive decision from Milestone 1
actually gets made. Everything above it — the labels, the appeal path — is
downstream of a number this function produced.

`score_to_label` is where you stop writing for a machine and start writing for
a person. A score of 0.62 means nothing to a writer.

⚠️ Your README's **Signals and Scoring** section has to name the file and
function holding your combining rule. The grader checks your code against what
you claim, so that line should read `scoring.py::combine_signals`.
"""

import config


def combine_signals(
    model_score: float, style_score: float, lexical_score: float | None = None
) -> float:
    """
    Combine the signals into one 0–1 score. (Milestone 4; stretch adds a third.)

    All inputs point the same way: higher means more likely AI. The output
    does too.

    Args:
        model_score: from `detector.model_signal` — how predictable the text is.
        style_score: from `stylometry.style_signal` — the shape of the text.
        lexical_score: from `lexical.lexical_signal` (stretch) — how close the
            text sits to a generic center. Optional: if omitted, the model and
            style weights are renormalized to split the full 1.0 between them,
            so this function still behaves for a two-signal caller.

    Returns:
        A float from 0.0 (confidently human) to 1.0 (confidently AI).

    The rule, decided before this was coded:

      - **Weighted average, not a veto rule.** Two signals disagreeing (one at
        0.9, one at 0.1) lands near 0.5 — "unsure" — on purpose. Two different
        methods disagreeing about a piece of text *is* uncertainty, and
        "unsure" is the one label that costs a writer nothing: it isn't an
        accusation, and it isn't cleared either. It just says a person should
        look, which is the honest answer when the evidence splits.
      - **Weights are 0.45 model / 0.35 style / 0.20 lexical** (config.py).
        The model signal reads for meaning, so it carries the most weight.
        The style signal gets the next-most because it's cheaper to fool than
        the model signal but harder to fool than the lexical one. The lexical
        signal is weighted lowest because a few deliberately chosen words
        move it without touching the sentence structure underneath — it adds
        information when the other two split, but it shouldn't dominate.
      - **Which way the weighting leans:** heavier weight on the model signal
        means a text that reads as human to signal one pulls the combined
        score down even if the style signal leans AI — fewer false
        accusations, at the cost of letting more AI text read as "unsure"
        instead of flagged. That's the deliberate trade from criteria.md #1.

    A case where my signals split: a short, plainly-worded paragraph I wrote
    myself scored high on the model signal (low perplexity — plain writing is
    predictable) but low on the style signal (real variation in sentence
    length). The weighted average pulled it down into "unsure" rather than
    "ai" — which is what this rule is for.
    """
    if lexical_score is None:
        total = config.WEIGHT_MODEL_SIGNAL + config.WEIGHT_STYLE_SIGNAL
        combined = (
            (config.WEIGHT_MODEL_SIGNAL / total) * model_score
            + (config.WEIGHT_STYLE_SIGNAL / total) * style_score
        )
    else:
        combined = (
            config.WEIGHT_MODEL_SIGNAL * model_score
            + config.WEIGHT_STYLE_SIGNAL * style_score
            + config.WEIGHT_LEXICAL_SIGNAL * lexical_score
        )
    return round(min(max(combined, 0.0), 1.0), 4)


def score_to_label(score: float) -> tuple[str, str]:
    """
    Turn a score into a guess and the text a reader actually sees.
    ← TODO (Milestone 5)

    Returns:
        (guess, label_text) — where `guess` is a short machine-readable string
        like "ai" / "human" / "unsure", and `label_text` is the full sentence
        shown to a person.

    ⚠️ Write the label text for someone who has never heard the word
    "threshold".

        ✗ "human, 0.81 confidence"
        ✓ "We think this was probably written by a person."

    All three labels have to be **reachable**. If no score can produce one of
    them, your ranges have a gap — and Milestone 5 asks you to submit text that
    produces each one, which is how you'd find out.

    The hardest one to write is "unsure". It has to admit uncertainty without
    sounding like an accusation, because the person reading it may well have
    written every word themselves. Your breakout asks your group what they'd
    think if they got it on their own work. That question is the whole
    milestone.
    """
    if score >= config.AI_THRESHOLD:
        return "ai", (
            "This looks like it was written by an AI system, not a person. "
            "If you wrote this yourself, you can appeal and a person will "
            "take a closer look."
        )
    if score <= config.HUMAN_THRESHOLD:
        return "human", "This looks like it was written by a person."
    return "unsure", (
        "We can't tell confidently whether a person or an AI wrote this. "
        "That's not a strike against you — if you wrote it yourself, you're "
        "welcome to appeal so a person can take a closer look."
    )


def label_ranges() -> list[tuple[str, str]]:
    """
    The score range each label covers. Your README needs these beside the
    label text — given to you so the numbers can't drift apart from config.py.
    """
    return [
        ("high-confidence human", f"0.00 – {config.HUMAN_THRESHOLD:.2f}"),
        ("unsure", f"{config.HUMAN_THRESHOLD:.2f} – {config.AI_THRESHOLD:.2f}"),
        ("high-confidence AI", f"{config.AI_THRESHOLD:.2f} – 1.00"),
    ]
