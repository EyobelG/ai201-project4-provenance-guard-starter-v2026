#!/usr/bin/env python3
"""
Route-level regression tests for `/batch`, via Flask's `test_client` — no
live server needed. ← UNIT 9 capstone, good-faith extension.

    python test_batch.py

`test.py` already uses `app.test_client()` for `/ping`; this extends the
same idea to `/batch` so criteria 1, 2, 3 and 5 from `criteria.md` have a
regression check that runs without `python app.py` in another terminal.
Criterion 4 (timing) stays in `run_batch_eval.py` — a timing comparison
against live HTTP overhead doesn't mean the same thing through the test
client, which skips the network entirely.

This one real model call (criterion 1's valid batch) is the slow part —
a few seconds the first time in a session, same as any other call into
`detector.py`. Nothing here downloads anything; it uses whatever model
`python detector.py` already cached.
"""

import app as appmod
import config

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


client = appmod.app.test_client()

VALID_TEXTS = [
    "I missed the bus this morning so I walked the whole way instead.",
    "My roommate keeps leaving dishes in the sink and I've decided not to say anything.",
    "The coffee shop near my apartment closed last month and I'm still bitter about it.",
]


# ── Criterion 1: batch correctness ─────────────────────────────────────────

items = [{"text": t, "creator_id": f"test_batch_{i}"} for i, t in enumerate(VALID_TEXTS)]
batch_resp = client.post("/batch", json={"items": items})
batch_body = batch_resp.get_json()

solo_guesses = []
for item in items:
    solo_resp = client.post("/submit", json=item)
    solo_guesses.append(solo_resp.get_json()["guess"])

check(
    "criterion 1: /batch returns 200 for a valid batch",
    batch_resp.status_code == 200,
)
check(
    "criterion 1: every batch item's guess matches the matching solo /submit",
    [r["guess"] for r in batch_body["results"]] == solo_guesses,
)


# ── Criterion 2: partial-failure isolation ──────────────────────────────────

mixed_items = [{"text": t, "creator_id": f"test_batch_mixed_{i}"} for i, t in enumerate(VALID_TEXTS)] + [
    {"creator_id": "bad_1"},                    # missing text
    {"text": "", "creator_id": "bad_2"},        # empty text
    {"text": 12345, "creator_id": "bad_3"},     # not a string
]
mixed_resp = client.post("/batch", json={"items": mixed_items})
mixed_body = mixed_resp.get_json()
decided = [r for r in mixed_body["results"] if "error" not in r]
errored = [r for r in mixed_body["results"] if "error" in r]

check("criterion 2: a mixed batch still returns 200", mixed_resp.status_code == 200)
check("criterion 2: 3 decided + 3 errors out of 6 items", len(decided) == 3 and len(errored) == 3)


# ── Criterion 3: batch size cap ─────────────────────────────────────────────

oversized = [{"text": VALID_TEXTS[0], "creator_id": f"over_{i}"}
            for i in range(config.MAX_BATCH_ITEMS + 1)]
over_resp = client.post("/batch", json={"items": oversized})

check("criterion 3: over the cap returns 400", over_resp.status_code == 400)
check(
    "criterion 3: nothing from the oversized batch appears in /log as decided",
    not any(e.get("batch_id") and e.get("status") == "decided"
            for e in appmod.audit.read_entries(limit=len(oversized) + 5)
            if e.get("creator_id", "").startswith("over_")),
)


# ── Criterion 5 (revised): malformed batch shapes ───────────────────────────

check(
    "criterion 5: items that isn't a list returns 400",
    client.post("/batch", json={"items": "nope"}).status_code == 400,
)
check(
    "criterion 5: an empty items list returns 400",
    client.post("/batch", json={"items": []}).status_code == 400,
)
check(
    "criterion 5 (revised): a non-dict item inside items is isolated, not a 400",
    client.post("/batch", json={"items": ["just a string"]}).status_code == 200,
)


print(f"\n{PASS} passed, {FAIL} failed")
if FAIL:
    raise SystemExit(1)
