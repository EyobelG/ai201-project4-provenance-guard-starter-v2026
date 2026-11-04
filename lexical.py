"""
Signal three (stretch): the lexical signal.

Signal one reads for meaning. Signal two reads the shape of the text. This one
reads neither — it measures how close the text sits to a *generic* center of
ordinary English, on two measures:

    function_word_ratio   what share of words are glue words (the, of, and...)
    avg_word_length       mean characters per word

**Higher means more likely AI**, same convention as the other two signals.

Why this might differ between human and AI writing: a language model trained
to predict the next likely word tends to land near the population average on
both of these — neither unusually heavy on function words nor unusually light,
neither full of long words nor full of short ones. A specific human voice
tends to sit off-center in one direction or the other: a terse writer who
drops articles, a writer who reaches for longer or rarer words than average.

⚠️ The blind spot: this signal has no idea whether the text makes sense. It
only asks "how close to the average is this?" — so writing that happens to be
very ordinary, including ordinary human writing, scores the same as text that
is ordinary because a model produced it. It is the same blind spot as signal
one for a different reason: both reward the unremarkable.

How it's weighted into the combined score: `scoring.combine_signals` weights
this signal at 0.20, against 0.45 for the model signal and 0.35 for the style
signal (see config.py). It's weighted lowest because it's the easiest of the
three to fool on purpose — swap in a few rare words and the average word
length moves, with no cost to the AI-ness of the sentence structure
underneath. It still adds value when the other two split, because it's
measuring something neither of them touches.
"""

import config

FUNCTION_WORDS = {
    "the", "a", "an", "and", "or", "but", "if", "of", "to", "in", "on", "at",
    "is", "are", "was", "were", "be", "been", "being", "it", "its", "this",
    "that", "these", "those", "as", "with", "for", "by", "from", "about",
    "into", "over", "after", "before", "between", "out", "up", "down", "so",
    "than", "then", "there", "here", "not", "no", "do", "does", "did", "has",
    "have", "had", "i", "you", "he", "she", "we", "they", "them", "his",
    "her", "their", "our", "your", "my", "which", "who", "whom", "what",
}


def words(text: str) -> list[str]:
    import re
    return re.findall(r"[a-z0-9']+", text.lower())


def function_word_ratio(text: str) -> float:
    """Share of words that are function (glue) words. 0 on empty text."""
    w = words(text)
    if not w:
        return 0.0
    return sum(1 for word in w if word in FUNCTION_WORDS) / len(w)


def avg_word_length(text: str) -> float:
    """Mean characters per word. 0 on empty text."""
    w = words(text)
    if not w:
        return 0.0
    return sum(len(word) for word in w) / len(w)


def lexical_signal(text: str) -> float:
    """
    The lexical signal as a 0–1 score. **Higher means more likely AI.**

    Distance from a generic center on both measures; small distance (close to
    the center) reads as more AI-ish, large distance (an idiosyncratic voice)
    reads as more human. The two distances are each capped at 1.0 before
    averaging so one runaway measure can't dominate the score.
    """
    if not text.strip():
        return 0.5

    fwr = function_word_ratio(text)
    awl = avg_word_length(text)

    fwr_center = config.LEXICAL_FWR_CENTER
    awl_center = config.LEXICAL_AWL_CENTER

    fwr_distance = min(abs(fwr - fwr_center) / 0.25, 1.0)
    awl_distance = min(abs(awl - awl_center) / awl_center, 1.0)

    distance = (fwr_distance + awl_distance) / 2.0
    score = 1.0 - distance
    return round(min(max(score, 0.0), 1.0), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"function_word_ratio   {function_word_ratio(text):.4f}")
    print(f"avg_word_length       {avg_word_length(text):.4f}")
    print(f"lexical_signal        {lexical_signal(text)}   (higher = more likely AI)")
