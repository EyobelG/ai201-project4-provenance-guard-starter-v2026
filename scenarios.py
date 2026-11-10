"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        "texts": [
            "I missed the bus this morning so I walked the whole way, which "
            "ended up being nice because the air was cold and I had time to "
            "think about nothing in particular.",
            "My roommate keeps leaving dishes in the sink and I've decided I'm "
            "not going to say anything about it today, mostly because I said "
            "something about it yesterday and it didn't help.",
            "The coffee shop near my apartment closed last month and honestly "
            "I'm still a little bitter about it. Nowhere else has the same "
            "burnt smell that somehow worked.",
            "I tried to fix the squeaky door hinge with cooking oil because I "
            "didn't have WD-40, and it worked for about two days before the "
            "squeak came back worse.",
            "We argued about where to eat for twenty minutes and then ended up "
            "at the same diner we always go to. I don't think either of us "
            "actually wanted to decide.",
            "There's a stray cat that sits on my windowsill every evening "
            "around six. I never feed it on purpose but I think it knows I "
            "will eventually.",
            "I rewrote the same paragraph of my essay four times last night "
            "and the version I kept was basically the first one, just with "
            "two commas moved.",
            "My little brother asked me to help him study for a test he "
            "insists he doesn't care about, and then quizzed himself out loud "
            "for an hour after I left.",
            "The bus was late again, which at this point feels less like bad "
            "luck and more like a personality trait of the route itself.",
            "I burned the garlic again. Every single time I tell myself I'll "
            "watch the pan and every single time I check my phone for ten "
            "seconds too long.",
        ],
    },
    {
        "name": "score spread — AI vs human, same topic",
        "criterion": 2,
        "texts": [
            # AI-generated (via an LLM), same topic as the human one below.
            "The adoption of remote work has fundamentally transformed "
            "workplace dynamics in recent years. Organizations must now "
            "consider a variety of important factors, including employee "
            "productivity, communication infrastructure, and the overall "
            "impact on company culture. It is essential to implement clear "
            "policies that address these considerations in order to ensure "
            "a smooth transition for all stakeholders involved.",
            # Human-written, same topic (remote work), deliberately specific/lumpy.
            "Working from home sounded great until my cat learned to open the "
            "office door with her paw. Now every call has a forty-pound "
            "interruption. I like not commuting. I do not like explaining why "
            "there's a cat on the keyboard during a client meeting — again.",
        ],
    },
    {
        "name": "label coverage",
        "criterion": 3,
        "texts": [
            "The implementation of the proposed framework requires careful "
            "consideration of several key factors. First, it is important to "
            "note that the system must be able to handle a wide variety of "
            "different inputs. Additionally, the overall performance of the "
            "solution depends on a number of important variables.",
            "Honestly? I was not sure this would even run the first time. It "
            "broke twice, then on the third try it just worked and I still "
            "do not fully know why.",
            "The results were mixed; some parts worked as expected while "
            "others required additional tuning before they behaved "
            "correctly, and it is unclear whether the remaining cases are "
            "genuine bugs.",
        ],
    },
    {
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"creator_id": "eval_bad_missing"},          # no text field at all
            {"text": "word " * 50000, "creator_id": "eval_bad_huge"},
            {"text": None, "creator_id": "eval_bad_null"},
        ],
    },

    # Criterion 4 (the appeal path) needs a submission's content_id before it
    # can send an appeal, which this scenario shape can't express — it's
    # tested by hand instead; see README's "Run Log and Verdicts" section for
    # that evidence.
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
