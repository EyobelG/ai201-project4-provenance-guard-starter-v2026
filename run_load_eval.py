#!/usr/bin/env python3
"""
A load observation for `/batch`. ← UNIT 9 capstone, stretch.

    python app.py                                  # in one terminal
    AI201_RATE_LIMITS=0 python app.py               # or this, to observe
                                                     # throughput without the
                                                     # rate limiter answering
                                                     # for it
    python run_load_eval.py                         # in another

This project's own cost arithmetic (README, "What It Costs") is 100
submissions/day at ~50.9ms each. This script sends ten times that many
scored items — 1,000 — as 100 ten-item `/batch` calls back to back, as fast
as the client can fire them, and reports whether per-item latency holds or
drifts under that burst. It does not decide pass/fail; there's no criterion
in `criteria.md` for this, only a number to look at.
"""

import argparse
import datetime as dt
import statistics
import sys
import time

import config

DEFAULT_URL = f"http://{config.HOST}:{config.PORT}"

TEXT = (
    "The bus was late again, which at this point feels less like bad luck "
    "and more like a personality trait of the route itself."
)


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--calls", type=int, default=100,
                        help="number of /batch calls (default 100, 10 items each = 1,000 items)")
    parser.add_argument("--items-per-call", type=int, default=10)
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--timeout", type=float, default=30.0)
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

    items = [{"text": TEXT, "creator_id": f"load_{i}"} for i in range(args.items_per_call)]
    per_item_durations = []  # duration_ms the service itself reports, one per scored item
    call_elapsed = []        # wall time of each /batch call, client-side

    print(f"{args.calls} batch calls x {args.items_per_call} items "
          f"= {args.calls * args.items_per_call} items total")

    run_started = time.perf_counter()
    for call_index in range(1, args.calls + 1):
        t0 = time.perf_counter()
        response = session.post(f"{args.url}/batch", json={"items": items}, timeout=args.timeout)
        call_elapsed.append((time.perf_counter() - t0) * 1000)
        body = response.json() if response.content else {}
        for result in body.get("results", []):
            if "duration_ms" in result:
                per_item_durations.append(result["duration_ms"])
        if call_index % 10 == 0:
            print(f"  [{call_index:>3}/{args.calls}] {response.status_code}")

    total_s = time.perf_counter() - run_started

    first_half = per_item_durations[: len(per_item_durations) // 2]
    second_half = per_item_durations[len(per_item_durations) // 2:]

    report = {
        "calls": args.calls,
        "items_per_call": args.items_per_call,
        "items_total": len(per_item_durations),
        "wall_time_s": round(total_s, 1),
        "items_per_second": round(len(per_item_durations) / total_s, 1) if total_s else None,
        "per_item_duration_ms": {
            "mean": round(statistics.mean(per_item_durations), 1),
            "median": round(statistics.median(per_item_durations), 1),
            "max": round(max(per_item_durations), 1),
            "first_half_mean": round(statistics.mean(first_half), 1) if first_half else None,
            "second_half_mean": round(statistics.mean(second_half), 1) if second_half else None,
        },
        "call_elapsed_ms": {
            "mean": round(statistics.mean(call_elapsed), 1),
            "max": round(max(call_elapsed), 1),
        },
    }

    print()
    print(f"items/sec:              {report['items_per_second']}")
    print(f"per-item mean (ms):     {report['per_item_duration_ms']['mean']}")
    print(f"per-item max (ms):      {report['per_item_duration_ms']['max']}")
    print(f"first half mean (ms):   {report['per_item_duration_ms']['first_half_mean']}")
    print(f"second half mean (ms):  {report['per_item_duration_ms']['second_half_mean']}")

    config.RESULTS_DIR.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    path = config.RESULTS_DIR / f"load_run_{stamp}.md"
    path.write_text(
        "# Load run — ten times the normal daily rate, in one burst\n\n"
        "- Produced by: `run_load_eval.py`\n"
        f"- {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
        "```json\n" + __import__("json").dumps(report, indent=2) + "\n```\n",
        encoding="utf-8",
    )
    print(f"\nWrote {path.relative_to(config.ROOT)}")


if __name__ == "__main__":
    main()
