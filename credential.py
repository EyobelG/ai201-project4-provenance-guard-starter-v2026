"""
Verified-human credential (stretch).

A writer who wants a badge on their submissions goes through one extra step:
`POST /verify` with their `creator_id` and an exact attestation phrase. This is
not real identity proof — nothing here could be. It's friction: cheap for a
genuine writer to clear once, mildly annoying to script at scale, and
recorded, so it can be checked or revoked later. Once granted, every
`/submit` from that `creator_id` carries `verified_human: true` and the label
says so.

    from credential import grant, is_verified

    grant("alice")
    is_verified("alice")   # True
"""

import json
import threading

import config

_lock = threading.Lock()
_PATH = config.LOG_DIR / "verified.json"

ATTESTATION_PHRASE = "I wrote this myself"


def _read() -> dict:
    if not _PATH.exists():
        return {}
    try:
        return json.loads(_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def _write(data: dict) -> None:
    config.LOG_DIR.mkdir(parents=True, exist_ok=True)
    with _lock:
        _PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")


def grant(creator_id: str) -> dict:
    """Mark a creator as a verified human. Idempotent."""
    data = _read()
    data[creator_id] = {"verified": True}
    _write(data)
    return data[creator_id]


def is_verified(creator_id: str) -> bool:
    """Whether this creator has cleared the attestation step."""
    return bool(_read().get(creator_id, {}).get("verified"))
