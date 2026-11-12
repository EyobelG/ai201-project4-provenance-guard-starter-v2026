#!/usr/bin/env python3
"""
Run the capstone criteria against /batch, 3 trials each. ← UNIT 9

    python app.py                                  # in one terminal
    python run_batch_eval.py --label before         # in another
    python run_batch_eval.py --label after

Covers criteria.md's "Capstone criteria — Unit 9" 1 through 5: batch
correctness, partial-failure isolation, the size cap, batching overhead
(timed against the matching solo /submit calls), and malformed batch shapes.

This does the sending, timing, and recording. It does not decide whether a
trial passed — that's the Verdict column, filled in by hand against the
targets in criteria.md.
"""

import argparse
import datetime as dt
import json
import sys
import time

import config

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(errors="replace")
    except (AttributeError, ValueError):
        pass

DEFAULT_URL = f"http://{config.HOST}:{config.PORT}"

VALID_TEXTS = [
    "I missed the bus this morning so I walked the whole way, which ended "
    "up being nice because the air was cold and I had time to think about "
    "nothing in particular.",
    "My roommate keeps leaving dishes in the sink and I've decided I'm not "
    "going to say anything about it today, mostly because I said something "
    "about it yesterday and it didn't help.",
    "The coffee shop near my apartment closed last month and honestly I'm "
    "still a little bitter about it. Nowhere else has the same burnt smell "
    "that somehow worked.",
    "I tried to fix the squeaky door hinge with cooking oil because I "
    "didn't have WD-40, and it worked for about two days before the squeak "
    "came back worse.",
    "We argued about where to eat for twenty minutes and then ended up at "
    "the same diner we always go to. I don't think either of us actually "
    "wanted to decide.",
    "There's a stray cat that sits on my windowsill every evening around "
    "six. I never feed it on purpose but I think it knows I will "
    "eventually.",
    "I rewrote the same paragraph of my essay four times last night and "
    "the version I kept was basically the first one, just with two commas "
    "moved.",
    "My little brother asked me to help him study for a test he insists he "
    "doesn't care about, and then quizzed himself out loud for an hour "
    "after I left.",
    "The bus was late again, which at this point feels less like bad luck "
    "and more like a personality trait of the route itself.",
    "I burned the garlic again. Every single time I tell myself I'll watch "
    "the pan and every single time I check my phone for ten seconds too "
    "long.",
]


def items_for(texts):
    return [{"text": t, "creator_id": f"batcheval_{i}"} for i, t in enumerate(texts, 1)]


def post(session, url, path, body, timeout):
    import requests
    started = time.perf_counter()
    try:
        response = session.post(f"{url}{path}", json=body, timeout=timeout)
        elapsed_ms = (time.perf_counter() - started) * 1000
        payload = response.json() if response.content else {}
        return {"status": response.status_code, "elapsed_ms": round(elapsed_ms, 1), "body": payload}
    except Exception as exc:  # noqa: BLE001
        elapsed_ms = (time.perf_counter() - started) * 1000
        return {"status": None, "elapsed_ms": round(elapsed_ms, 1),
                "error": f"{type(exc).__name__}: {exc}"}


def run_trial(session, url, timeout):
    """One trial of all five criteria. Returns a dict of criterion -> outcome."""
    outcome = {}

    # Criterion 1 + 4: a valid 10-item batch, and the matching 10 solo /submit
    # calls, so correctness and per-item overhead can both be read off one trial.
    items = items_for(VALID_TEXTS)
    batch_result = post(session, url, "/batch", {"items": items}, timeout)

    solo_results = []
    for item in items:
        solo_results.append(post(session, url, "/submit", item, timeout))
    solo_total_ms = sum(r["elapsed_ms"] for r in solo_results)

    outcome["1_and_4"] = {
        "batch": batch_result,
        "solo": solo_results,
        "solo_total_ms": round(solo_total_ms, 1),
        "solo_per_item_ms": round(solo_total_ms / len(items), 1),
        "batch_per_item_ms": (
            round(batch_result["elapsed_ms"] / len(items), 1)
            if batch_result.get("status") == 200 else None
        ),
    }

    # Criterion 2: 7 valid + 3 malformed items in one batch.
    mixed_items = items_for(VALID_TEXTS[:7]) + [
        {"creator_id": "batcheval_bad_1"},          # missing text
        {"text": "", "creator_id": "batcheval_bad_2"},       # empty text
        {"text": 12345, "creator_id": "batcheval_bad_3"},    # not a string
    ]
    outcome["2"] = post(session, url, "/batch", {"items": mixed_items}, timeout)

    # Criterion 3: over the cap.
    oversized = items_for(VALID_TEXTS * ((config.MAX_BATCH_ITEMS // 10) + 1))
    outcome["3"] = post(session, url, "/batch", {"items": oversized}, timeout)

    # Criterion 5: malformed batch shapes.
    outcome["5"] = {
        "non_dict_item": post(session, url, "/batch", {"items": ["just a string"]}, timeout),
        "items_not_a_list": post(session, url, "/batch", {"items": "nope"}, timeout),
        "empty_items": post(session, url, "/batch", {"items": []}, timeout),
    }

    return outcome


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--label", default="")
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--timeout", type=float, default=120.0)
    args = parser.parse_args()

    try:
        import requests
    except ImportError:
        print("The `requests` package isn't installed.\nRun: pip install -r requirements.txt",
              file=sys.stderr)
        sys.exit(1)

    session = requests.Session()
    try:
        session.get(f"{args.url}/health", timeout=5)
    except Exception:  # noqa: BLE001
        print(f"Nothing answering at {args.url}. Start it:  python app.py", file=sys.stderr)
        sys.exit(1)

    if args.trials < 3:
        print(f"!! {args.trials} trial(s). The submission asks for three.\n")

    trials = []
    for trial in range(1, args.trials + 1):
        print(f"trial {trial}...")
        trials.append(run_trial(session, args.url, args.timeout))

    write_report(trials, args)


def write_report(trials, args):
    config.RESULTS_DIR.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    label = f"_{args.label}" if args.label else ""
    path = config.RESULTS_DIR / f"batch_run_{stamp}{label}.md"

    lines = [
        f"# Batch run log{f' — {args.label}' if args.label else ''}",
        "",
        "- Produced by: `run_batch_eval.py::main`",
        "- Service: `app.py::batch` (Unit 9 capstone extension)",
        f"- {args.trials} trials · {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "Real output per trial. Targets and verdicts come from `criteria.md`.",
        "",
    ]

    for i, outcome in enumerate(trials, 1):
        lines += [f"## Trial {i}", "", "```json", json.dumps(outcome, indent=2), "```", ""]

    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote {path.relative_to(config.ROOT)}")
    print("Commit it. It's the evidence the test actually happened.")


if __name__ == "__main__":
    main()
