# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. A writing site sends `POST /submit` with `text` and `creator_id` as JSON.
2. The route validates the body — missing/empty `text`, missing `creator_id`,
   or `text` over 20,000 characters all return a `400` before any signal runs.
3. A `content_id` (UUID) is generated for the submission.
4. Three signals score the text independently, each 0.0–1.0, higher = more
   likely AI: `detector.model_signal` (a local language model's perplexity),
   `stylometry.style_signal` (sentence-length spread, vocabulary variety,
   punctuation density), and `lexical.lexical_signal` (stretch — distance from
   a generic function-word/word-length center).
5. `scoring.combine_signals` weights and averages the three into one score.
6. `scoring.score_to_label` maps that score to a guess (`ai`/`human`/`unsure`)
   and the full-sentence label text a reader sees. If the `creator_id` holds a
   verified-human credential (stretch, via `POST /verify`), a line is appended
   noting that.
7. The decision — both raw signal scores, the combined score, the guess, and
   the label — is written to `logs/audit.jsonl` through `audit.log_decision`.
8. The response carries the `content_id`, guess, confidence, label, and all
   three signal scores back to the caller.

A writer who disagrees sends `POST /appeal` with that `content_id` and their
reasoning. The route confirms the id exists, appends an appeal entry that
moves `status` to `under_review`, and confirms — no automatic re-checking.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** Perplexity — how predictable the text is to a local
GPT-2 model. Low perplexity (the model isn't surprised) scores high on the
AI scale.

**Why that might differ between human and AI writing:** A language model
writes by repeatedly picking a likely next word, so its output tends to be
text that a model finds easy to predict. Human writing wanders more — odd
word choices, abrupt turns, the specific instead of the typical.

**What it can't see:** The difference between "predictable because an AI
wrote it" and "predictable because a person wrote plainly on purpose." Second-
language writers, younger writers, and anyone writing in short common words
score as machine-like as actual machine writing does on this signal alone.

### Signal two — the style signal

**What it measures:** The text's shape, not its meaning — sentence-length
spread (coefficient of variation), vocabulary variety (type-token ratio), and
punctuation density (`;`, `:`, em/en dash per word).

**Why that might differ between human and AI writing:** Generated prose tends
toward even, mid-length sentences and a narrower vocabulary band, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one, bursts of varied
punctuation.

**What it can't see:** The text's content at all. Anything that changes the
shape without changing the substance moves this signal — typos, broken-up
sentences, a pasted quotation — which is a cheap thing to do on purpose.

### Signal three — the lexical signal (stretch)

**What it measures:** How close the text sits to a generic center of ordinary
English on two measures — function-word ratio and average word length.

**Why that might differ between human and AI writing:** A model trained to
predict the next likely word tends to land near the population average on
both; a specific human voice tends to sit off-center in one direction.

**What it can't see:** Whether the text makes sense. It only measures
distance from average, so ordinary human writing scores the same as text
that's ordinary because a model produced it — the same blind spot as signal
one, for a different reason.

### The combining rule

**The rule:** A weighted average, not a veto. When two signals disagree (one
high, one low), the average pulls the combined score toward 0.5 — "unsure" —
on purpose, because two different methods disagreeing about a text *is*
uncertainty, and "unsure" is the label that costs a writer nothing: it isn't
an accusation and it isn't a clearance, it just says a person should look.

**The numbers:** `model_score * 0.45 + style_score * 0.35 + lexical_score *
0.20`. The model signal carries the most weight because it reads for meaning.
The style signal is next because it's cheaper to fool than signal one but
harder than signal three. The lexical signal is weighted lowest because a
handful of deliberately chosen words move it without touching the sentence
structure underneath — it should nudge the score when the other two split,
not dominate it.

**Where it lives:** `scoring.py::combine_signals`

**A case where my two signals split, and what my rule does with it:** A
short, plainly-worded human paragraph scored high on the model signal (0.89 —
plain writing is predictable) but noticeably lower on the style signal (0.67 —
real sentence-length variation and distinct punctuation). The weighted average
(0.79, with the lexical signal added in) still crossed into `ai` here, which
is an honest limitation of a 0.45-weighted model signal on short, plain text —
see **What's Still Broken** territory for unit 8. On a case with less extreme
model-signal input, the same split pulls the result down into `unsure` rather
than `ai`, which is the behavior the rule is designed for.

---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35, inclusive of 0.35 | "This looks like it was written by a person." |
| unsure | above 0.35, below 0.65 | "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you — if you wrote it yourself, you're welcome to appeal so a person can take a closer look." |
| high-confidence AI | 0.65 – 1.00, inclusive of 0.65 | "This looks like it was written by an AI system, not a person. If you wrote this yourself, you can appeal and a person will take a closer look." |

<!-- `scoring.py::score_to_label` checks `>= AI_THRESHOLD` first, then
     `<= HUMAN_THRESHOLD`, so a score of exactly 0.35 is `human` and exactly
     0.65 is `ai` — "unsure" is the strictly-between band. `scoring.py::
     label_ranges()` prints these same ranges so the README and the code
     can't drift apart; `test_signals.py` has boundary assertions at both
     values. -->

A verified-human credential (stretch — see **Stretch Features** below) appends
one more sentence to any of the three: *"This writer holds a verified-human
credential."*

**Why I worded the "unsure" one this way:**

The first draft read "We're not confident about this one" — accurate, but it
puts the whole burden of guessing what that means on the writer. The final
version says explicitly that it isn't an accusation and names the one thing
the writer can actually do next: appeal. "Confidently" is the one word doing
the most work — it says the uncertainty is the system's, not a soft way of
calling the writing suspicious.

---

## Stretch Features

Three stretch features, all built:

1. **A third signal** — `lexical.py`, documented above under "Signal three."
   Weighted 0.20 in `scoring.combine_signals`, lowest of the three, with the
   weighting reasoning under **The combining rule**.
2. **`GET /content/<id>`** — returns one item's current `status` and its full
   history (the original decision plus any appeal), read straight off
   `audit.entries_for`.
3. **A verified-human path** — `POST /verify` with `{"creator_id", "attestation"}`.
   The attestation has to match the phrase `"I wrote this myself"` exactly
   (`credential.ATTESTATION_PHRASE`). This is not identity verification — it's
   deliberate friction: trivial for a genuine writer to clear once, and
   recorded in `logs/verified.json` so it persists across submissions. Once
   granted, every `/submit` from that `creator_id` carries `verified_human:
   true` in the response and log entry, and the label gets one appended
   sentence saying so.

Pasted requests and responses for all three are under **Sample Run**, below.

---

## Testing

`scoring.py`, `stylometry.py`, and `lexical.py` are pure functions — a string
in, a float out, no server or model download required to exercise them.
`test_signals.py` runs a handful of plain assertions against them: empty-text
and single-sentence edge cases, and the exact label-boundary scores (0.35 and
0.65) where `score_to_label`'s `<=`/`>=` comparisons decide which label wins.

```bash
$ python test_signals.py
```

17 of 17 pass as of this submission — see the pasted output in the project's
commit history, or run it yourself; it takes under a second.

Malformed input is also never silent: every `400` from `/submit`, `/appeal`,
and `/verify` is logged through `audit.log_rejection` (`status: "rejected"`),
not just returned to the caller — see the rejected entry in **Sample Run**'s
log excerpt below.

**`test_batch.py`** (added for the capstone) extends the same `test_client()`
approach `test.py` already uses for `/ping` to `/batch` — criteria 1, 2, 3
and 5 from `criteria.md`'s capstone section, as route-level assertions that
run without a live server in another terminal. Criterion 4 (timing) stays
in `run_batch_eval.py`, since a timing comparison against live HTTP
overhead doesn't mean the same thing through the test client.

```bash
$ python test_batch.py
```

9 of 9 pass as of this submission.

---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "The implementation of the proposed framework requires careful consideration of several key factors. First, it is important to note that the system must be able to handle a wide variety of different inputs. Additionally, the overall performance of the solution depends on a number of important variables.", "creator_id": "demo-writer-1"}'
```

```json
{
  "confidence": 0.7892,
  "content_id": "26a2f375-8751-4700-826f-c4e5d77ab9a3",
  "guess": "ai",
  "label": "This looks like it was written by an AI system, not a person. If you wrote this yourself, you can appeal and a person will take a closer look.",
  "lexical_score": 0.7728,
  "model_score": 0.8864,
  "style_score": 0.6736,
  "verified_human": false
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "26a2f375-8751-4700-826f-c4e5d77ab9a3", "reasoning": "I wrote this paragraph myself for a class assignment; it just happens to read formally."}'
```

```json
{
  "content_id": "26a2f375-8751-4700-826f-c4e5d77ab9a3",
  "entry": {
    "content_id": "26a2f375-8751-4700-826f-c4e5d77ab9a3",
    "creator_id": "demo-writer-1",
    "event": "appeal",
    "reasoning": "I wrote this paragraph myself for a class assignment; it just happens to read formally.",
    "status": "under_review",
    "timestamp": "2026-11-04T13:05:42+00:00"
  },
  "message": "Appeal recorded. A person will review this submission.",
  "ok": true,
  "status": "under_review"
}
```

**Stretch — earning the verified-human credential, then submitting**

```bash
$ curl -X POST http://127.0.0.1:5000/verify \
  -H "Content-Type: application/json" \
  -d '{"creator_id": "demo-writer-2", "attestation": "I wrote this myself"}'
```

```json
{"creator_id": "demo-writer-2", "ok": true, "verified_human": true}
```

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "Honestly? I was not sure this would even run the first time. It broke twice, then on the third try it just worked and I still do not fully know why.", "creator_id": "demo-writer-2"}'
```

```json
{
  "confidence": 0.5603,
  "content_id": "af1bcc74-df8d-4f79-954a-a0f099e91d1a",
  "guess": "unsure",
  "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you — if you wrote it yourself, you're welcome to appeal so a person can take a closer look. This writer holds a verified-human credential.",
  "lexical_score": 0.8718,
  "model_score": 0.5547,
  "style_score": 0.3896,
  "verified_human": true
}
```

Note the label's appended sentence and `"verified_human": true` — that's the
credential showing on the writer's work, per the stretch brief.

**Stretch — looking up that item's status**

```bash
$ curl http://127.0.0.1:5000/content/af1bcc74-df8d-4f79-954a-a0f099e91d1a
```

```json
{
  "content_id": "af1bcc74-df8d-4f79-954a-a0f099e91d1a",
  "status": "decided",
  "history": [
    {
      "combined_score": 0.5603,
      "content_id": "af1bcc74-df8d-4f79-954a-a0f099e91d1a",
      "creator_id": "demo-writer-2",
      "guess": "unsure",
      "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you — if you wrote it yourself, you're welcome to appeal so a person can take a closer look. This writer holds a verified-human credential.",
      "lexical_score": 0.8718,
      "model_score": 0.5547,
      "status": "decided",
      "style_score": 0.3896,
      "timestamp": "2026-11-04T13:05:42+00:00",
      "verified_human": true
    }
  ]
}
```

**A rejected request — malformed input is logged, not just returned**

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"creator_id": "demo-writer-2"}'
```

```json
{"error": "bad_request", "message": "'text' is required and must be a non-empty string."}
```

**What the log shows afterwards** — all four events from this run, including
the appeal and the rejection, oldest first:

```bash
$ curl "http://127.0.0.1:5000/log?limit=10"
```

```json
{
  "count": 4,
  "entries": [
    {
      "combined_score": 0.7892,
      "content_id": "26a2f375-8751-4700-826f-c4e5d77ab9a3",
      "creator_id": "demo-writer-1",
      "guess": "ai",
      "label": "This looks like it was written by an AI system, not a person. If you wrote this yourself, you can appeal and a person will take a closer look.",
      "lexical_score": 0.7728,
      "model_score": 0.8864,
      "status": "decided",
      "style_score": 0.6736,
      "timestamp": "2026-11-04T13:05:41+00:00",
      "verified_human": false
    },
    {
      "content_id": "26a2f375-8751-4700-826f-c4e5d77ab9a3",
      "creator_id": "demo-writer-1",
      "event": "appeal",
      "reasoning": "I wrote this paragraph myself for a class assignment; it just happens to read formally.",
      "status": "under_review",
      "timestamp": "2026-11-04T13:05:42+00:00"
    },
    {
      "combined_score": 0.5603,
      "content_id": "af1bcc74-df8d-4f79-954a-a0f099e91d1a",
      "creator_id": "demo-writer-2",
      "guess": "unsure",
      "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you — if you wrote it yourself, you're welcome to appeal so a person can take a closer look. This writer holds a verified-human credential.",
      "lexical_score": 0.8718,
      "model_score": 0.5547,
      "status": "decided",
      "style_score": 0.3896,
      "timestamp": "2026-11-04T13:05:42+00:00",
      "verified_human": true
    },
    {
      "creator_id": "demo-writer-2",
      "event": "rejected",
      "message": "'text' is required and must be a non-empty string.",
      "reason": "bad_request",
      "status": "rejected",
      "timestamp": "2026-11-04T13:05:42+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* A combining rule for `scoring.py::combine_signals` that
  handles signal disagreement sensibly, with the weights justified.
- *What came back:* A weighted average (0.45/0.35/0.20 model/style/lexical)
  with reasoning for the weight ordering and a note on what happens when
  signals split.
- *What I changed:* Kept the weighted-average approach and the 0.45/0.35/0.20
  split, but added the two-signal fallback path (renormalizing weights when
  the lexical score is omitted) so `combine_signals` still works for a caller
  that only has the two required signals, not just the three-signal stretch
  case.

**Moment 2**

- *What I asked for:* Label text for the "unsure" case that a non-technical
  reader wouldn't read as an accusation.
- *What came back:* A first draft that said "We're not confident about this
  one," then a second pass naming the appeal path explicitly after being
  asked to imagine the writer's reaction to that sentence alone.
- *What I changed:* Added the opening clause "That's not a strike against
  you" before the appeal mention, so the label leads with reassurance rather
  than making the writer find it after an uncertain-sounding first sentence.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 10 per minute, 200 per day (`config.py::RATE_LIMIT_PER_MINUTE` /
`RATE_LIMIT_PER_DAY`), enforced by Flask-Limiter, keyed by `creator_id`.

**Why those numbers and not others:** A real writer submitting their own work
a few times an hour never gets near 10 in a minute — even pasting and
resubmitting several drafts in a row stays under it. A script mapping my
thresholds, on the other hand, wants dozens or hundreds of calls in quick
succession to do that cheaply, and 10/minute makes that expensive without
ever touching a normal writer's workflow. 200/day is loose on purpose — it
exists to catch a runaway script left looping overnight, not to ration a
writer's day.

**What a caller counts as:** Per `creator_id`, not per IP address
(`app.py::rate_limit_key`). One household's writers on the same network stay
independent; the cost is that one attacker who rotates `creator_id` values
(as the attack set's non-`flood_same_creator` families all do, deliberately)
looks like a crowd of different callers and never trips the limit at all —
a limit keyed per-creator can't see that, and a production version would
need a secondary signal (IP, account age) to catch it.

**The run of status codes when I pushed past it:**

    python run_attacks.py --flood 15

```
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```

5 of 15 were rate limited — the 11th submission from the same `creator_id`
inside a minute, exactly where `10/minute` says it should. `GET /log` after
the run shows the matching `rejected` / `rate_limited` entries (see
`results/flood_2026-11-10_1010.md`).

---

## Attack Run — Before

The official unit 8 attack set sits behind a CodePath login I couldn't
script past, so I assembled my own `attack_set/attacks.csv` and
`attack_set/attacks_malformed_requests.csv` from the unit 7 demo samples
(`clearly_ai`, `clearly_human`, `borderline`, `evasion_typos`,
`lightly_edited_ai`, `injection`, `too_short`) plus three of my own
false-positive writing samples and five malformed-request / flood cases of
my own. `run_attacks.py --set attack_set --label before` produced
`results/attack_run_2026-11-10_1017_before.md`; the table below is that run
with HELD/BROKE added by hand.

| ID | Family | Targeting | Status | Guess | Score | Verdict |
|---|---|---|---|---|---|---|
| AI01 | clearly_ai | generic AI paragraph — should score `ai` | 200 | unsure | 0.624 | HELD (ran clean; landed `unsure` instead of `ai` — a calibration miss, not an evasion of anything) |
| HU01 | clearly_human | specific, voicey human paragraph — should score `human` | 200 | unsure | 0.472 | HELD |
| BL01 | borderline | AI text rewritten casual — should land `unsure` | 200 | unsure | 0.451 | HELD |
| EV01 | evasion_typos | 13 typos added to AI text | 200 | unsure | 0.392 | **BROKE** — pulled well below AI01's own score despite being the same paragraph with typos added |
| EV02 | lightly_edited_ai | AI text lightly humanized | 200 | unsure | 0.566 | HELD |
| INJ01 | injection | AI text + "Ignore previous instructions..." | 200 | unsure | 0.587 | HELD — the injection sentence doesn't move either signal; neither signal reads meaning |
| TS01 | too_short | 2-word submission | 400 | — | — | HELD — rejected cleanly, no 500 |
| FP01 | false_positive | ordinary human writing | 200 | **ai** | 0.735 | **BROKE** |
| FP02 | false_positive | ordinary human writing | 200 | **ai** | 0.760 | **BROKE** |
| FP03 | false_positive | ordinary human writing | 200 | **ai** | 0.703 | **BROKE** |
| MAL01–05 | malformed_requests | missing/empty/huge/non-JSON/list body | 400 | — | — | HELD — all 5 came back 400, none 500 |
| FLOOD01–05 | flood_same_creator | 5 submissions, one shared `creator_id` | 200 | unsure | — | HELD — only 5 requests, under the 10/minute limit, so no 429 was expected here |

**Ten audit log entries from the run** (`GET /log?limit=40`, full extract in
`results/audit_extract.json`):

```json
{"timestamp": "2026-11-10T15:17:46+00:00", "combined_score": 0.6239, "content_id": "b9bf75de-d670-466d-a51a-3fdf301f38d3", "creator_id": "attacker_AI01", "guess": "unsure", "model_score": 0.7544, "style_score": 0.5804, "status": "decided", "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you — if you wrote it yourself, you're welcome to appeal so a person can take a closer look."}
{"timestamp": "2026-11-10T15:17:46+00:00", "combined_score": 0.4724, "content_id": "3099fcc6-8292-4ddc-ae18-fafdc81fc8b0", "creator_id": "attacker_HU01", "guess": "unsure", "model_score": 0.4445, "style_score": 0.2521, "status": "decided", "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you — if you wrote it yourself, you're welcome to appeal so a person can take a closer look."}
{"timestamp": "2026-11-10T15:17:47+00:00", "combined_score": 0.3915, "content_id": "e2e012a7-30bb-4deb-bfd3-bd18a66c5e43", "creator_id": "attacker_EV01", "guess": "unsure", "model_score": 0.2324, "style_score": 0.5804, "status": "decided", "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you — if you wrote it yourself, you're welcome to appeal so a person can take a closer look."}
{"timestamp": "2026-11-10T15:17:47+00:00", "combined_score": 0.5873, "content_id": "dae87952-93f7-49e2-86c5-1eaebfff40f5", "creator_id": "attacker_INJ01", "guess": "unsure", "model_score": 0.6504, "style_score": 0.5922, "status": "decided", "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you — if you wrote it yourself, you're welcome to appeal so a person can take a closer look."}
{"timestamp": "2026-11-10T15:17:47+00:00", "creator_id": "attacker_TS01", "event": "rejected", "message": "Text is too short to score — a few sentences at least.", "reason": "bad_request", "status": "rejected", "label": null}
{"timestamp": "2026-11-10T15:17:47+00:00", "combined_score": 0.735, "content_id": "3b2c6973-75f8-4fad-918b-0f54bc7e16ac", "creator_id": "attacker_FP01", "guess": "ai", "model_score": 0.696, "style_score": 0.7375, "status": "decided", "label": "This looks like it was written by an AI system, not a person. If you wrote this yourself, you can appeal and a person will take a closer look."}
{"timestamp": "2026-11-10T15:17:47+00:00", "combined_score": 0.7601, "content_id": "37fcc214-756a-4453-ae7d-66846b63e698", "creator_id": "attacker_FP02", "guess": "ai", "model_score": 0.7293, "style_score": 0.7375, "status": "decided", "label": "This looks like it was written by an AI system, not a person. If you wrote this yourself, you can appeal and a person will take a closer look."}
{"timestamp": "2026-11-10T15:17:48+00:00", "combined_score": 0.7034, "content_id": "36c2a37e-076c-4d89-97d0-758429cdd1ba", "creator_id": "attacker_FP03", "guess": "ai", "model_score": 0.5895, "style_score": 0.72, "status": "decided", "label": "This looks like it was written by an AI system, not a person. If you wrote this yourself, you can appeal and a person will take a closer look."}
{"timestamp": "2026-11-10T15:17:48+00:00", "creator_id": "unknown", "event": "rejected", "message": "Request body must be a JSON object.", "reason": "bad_request", "status": "rejected", "label": null}
{"timestamp": "2026-11-10T15:17:48+00:00", "creator_id": "demo_instructor", "event": "rejected", "message": "'text' exceeds the 20000-character limit.", "reason": "bad_request", "status": "rejected", "label": null}
```

**The single worst outcome** — FP02: an ordinary, mildly complaint-y paragraph
about a roommate and dishes, nothing formal or generic about it, scored
0.760 and came back labeled high-confidence AI. That's the exact writer the
system is supposed to protect, told the opposite of the truth with the
highest confidence the service can express.

---

## Run Log and Verdicts

`run_eval.py --label before` against `scenarios.py` → `results/run_2026-11-10_1011_before.md`.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. my own writing | ≤1/10 `ai` | 4/10 ai | 4/10 ai | 4/10 ai | **MISS** |
| 2. score spread (AI vs human, same topic) | ≥0.40 apart | 0.193 apart (0.602 vs 0.409) | same | same | **MISS** |
| 3. label coverage | all 3 labels reachable | ai, unsure, unsure (no `human`) | same | same | **MISS** on these texts (`human` is reachable elsewhere — see EV01 in the attack run after the fix) |
| 4. appeal path (tested by hand, not through `scenarios.py`) | 5/5 → `under_review`, 5/5 in `GET /log` | 5/5, 5/5 | 5/5, 5/5 | 5/5, 5/5 | HIT |
| 5. bad input never crashes | 3/3 → 400, 0/3 → 500 | 4/4 → 400, 0 → 500 | same | same | HIT |

(Trials repeat exactly because `detector.model_signal` is deterministic
against identical input on this machine — no sampling involved — so three
trials of the same text return the same score each time. The flood and
attack-set runs, run at different times against different inputs, are the
evidence of day-to-day variation instead.)

**Real output from one trial** (`run_eval.py` → `app.py::submit`):

```json
{
  "status": 200,
  "guess": "ai",
  "confidence": 0.735,
  "model_score": 0.696,
  "style_score": 0.7375,
  "label": "This looks like it was written by an AI system, not a person. If you wrote this yourself, you can appeal and a person will take a closer look.",
  "sent": "I missed the bus this morning so I walked the whole way, which ended u"
}
```

**Diagnoses**

1. **Criterion 1 miss, and `FP01`–`FP03` in the attack run — stage: signal
   two, `stylometry.py::style_signal`'s `punctuation_density` sub-measure.**
   `punctuation_density` only counts `;`, `:`, em dash and en dash. Almost no
   short, ordinary conversational writing uses any of those — mine didn't,
   and FP01–FP03 didn't either. With zero marks, `density_norm` is `0`, so
   `ai_from_density` was hard-coded to `1.0` — the single most AI-like value
   the sub-measure can return — regardless of anything else about the text.
   That sub-measure carries 0.3 of `style_signal`'s weight and `style_signal`
   carries 0.35 of the combined score, so plain writing with no semicolons
   picked up roughly `0.3 × 0.35 ≈ 0.105` toward `ai` for a reason that has
   nothing to do with who wrote it. Combined with signal one's own blind
   spot (plain writing reads as predictable to GPT-2 regardless of
   authorship), that was enough to push 4 of 10 real paragraphs past
   `AI_THRESHOLD`.

2. **Criterion 2 miss — stage: signal two again, same mechanism.** The human
   sample (no semicolons/dashes) got the same `1.0`-from-density penalty as
   the AI sample, so the gap between them came almost entirely from signal
   one. One signal doing all the separating work is why the spread (0.193)
   fell well short of the 0.40 target — it isn't that the two texts read
   alike, it's that signal two couldn't tell them apart at all on this axis.

3. **Criterion 3 miss — stage: test design, not the service.** None of the
   three `label coverage` scenario texts landed below `HUMAN_THRESHOLD`
   (0.35); the "confident human" sample I wrote for it was specific but still
   used clean punctuation and middling sentence variety, so it landed
   `unsure` rather than `human`. The label itself is reachable — `EV01` in
   the attack run (typo-laden AI text) scored `human` after the fix below —
   it's that my test input for this criterion never tried to.

---

## The Improvement

**What I changed:** In `stylometry.py::style_signal`, when `punctuation_density`
is exactly `0` (no `;:—–` at all), `ai_from_density` now returns the neutral
midpoint `0.5` instead of the maximal-AI `1.0`. A text still gets full credit
toward "human" for actually using those marks; it just stops being penalized
for the much more common case of using none.

**Which diagnosis pointed at it:** Diagnosis 1 — the `0` → `1.0` mapping was
the identified mechanism, and it's a one-line fix at the point it happens
rather than a reweighting of the whole signal.

### Attack Run — After

`run_attacks.py --set attack_set --label after` → `results/attack_run_2026-11-10_1018_after.md`.

| ID | Family | Status | Guess | Score (before → after) | Verdict |
|---|---|---|---|---|---|
| AI01 | clearly_ai | 200 | unsure | 0.624 → 0.571 | HELD, drifted slightly further from `ai` |
| EV01 | evasion_typos | 200 | **human** | 0.392 → **0.339** | **BROKE** — now crosses `HUMAN_THRESHOLD` |
| FP01 | false_positive | 200 | ai | 0.735 → 0.682 | **still BROKE**, closer to the line |
| FP02 | false_positive | 200 | ai | 0.760 → 0.708 | **still BROKE** |
| FP03 | false_positive | 200 | ai | 0.703 → 0.651 | **still BROKE**, now 0.001 above `AI_THRESHOLD` |
| everything else | — | 200/400 as before | — | ~unchanged | HELD |

**Did it help, and how do I know:** Partly. All three false-positive scores
dropped (0.735→0.682, 0.760→0.708, 0.703→0.651), confirming the mechanism in
diagnosis 1 — but all three are still above `AI_THRESHOLD`, so criterion 1
is still a miss (3 of 10 own-writing samples flagged `ai` instead of ≤1).
The trade showed up immediately: `EV01`'s typo-laden AI paragraph, which
only *held* at `unsure` before, now flips all the way to `human`, because
the same sub-measure that was over-penalizing plain human writing was also
the thing keeping typo'd AI text from reading as clean prose. Widening
tolerance for the absence of semicolons helped real writers and handed the
typo-evasion family an extra win.

---

## A Second Improvement (stretch)

**What I changed:** Diagnosis 1 also named signal one (`model_score`, 0.45
weight) as a second contributor to the criterion 1 miss — plain, declarative
writing reads as predictable to GPT-2 regardless of who wrote it, and the
style fix alone left FP01–FP03 just above the line (0.682 / 0.708 / 0.651,
against `AI_THRESHOLD = 0.65`). Rather than touch the model itself, I raised
`AI_THRESHOLD` from `0.65` to `0.72` (`config.py`) — the same move the
criterion's own "why this target" argument asks for: false accusations cost
more than missed detections, so the bar for the accusation should sit higher.
I checked first that `ai` stayed reachable at `0.72` — the unit 7 Sample Run
exemplar text still scores 0.7367.

**Re-run, before and after this change** (`run_eval.py --label second`,
`run_attacks.py --set attack_set --label second` →
`results/run_2026-11-10_1028_second.md`,
`results/attack_run_2026-11-10_1028_second.md`):

| Case | After fix 1 (`AI_THRESHOLD=0.65`) | After fix 2 (`AI_THRESHOLD=0.72`) |
|---|---|---|
| Criterion 1 (own writing) | 3/10 scored `ai` — still a MISS | **0/10 scored `ai` — HIT** |
| FP01 | 0.682 → `ai` | 0.682 → `unsure` |
| FP02 | 0.708 → `ai` | 0.708 → `unsure` |
| FP03 | 0.651 → `ai` | 0.651 → `unsure` |
| AI01 (`clearly_ai`) | 0.571 → `unsure` | 0.571 → `unsure` (unchanged — was already below both thresholds) |
| EV01 (`evasion_typos`) | 0.339 → `human` | 0.339 → `human` (unchanged) |

**Third run log**, same format as **Run Log and Verdicts** above
(`run_eval.py --label second` → `results/run_2026-11-10_1028_second.md`):

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. my own writing | ≤1/10 `ai` | 0/10 ai | 0/10 ai | 0/10 ai | **HIT** |
| 2. score spread | ≥0.40 apart | 0.193 apart | same | same | still MISS |
| 3. label coverage | all 3 labels reachable | ai, unsure, unsure | same | same | still MISS on these texts |
| 5. bad input | 3/3 → 400, 0 → 500 | 4/4 → 400, 0 → 500 | same | same | HIT |

**Did it help, and how do I know:** Yes, for criterion 1 specifically — 0 of
10 own-writing samples now score `ai`, where the first fix alone left 3.
The cost is on the other side of the same trade as before, just pushed
further: a text now has to clear 0.72, not 0.65, to ever be told it looks
like AI, so anything that was already a weak "ai" call (there was nothing in
my attack set scoring between 0.65 and 0.72 to begin with) gets harder to
catch going forward. The `ai` label itself stays reachable — confirmed
against the unit 7 exemplar — so this isn't a label that's quietly become
unreachable, just one that requires a stronger signal than before.

---

## Stretch — Per-creator rate limits

Rate limiting here is keyed by `creator_id`, not by caller address
(`app.py::rate_limit_key`, falling back to the caller's address only when
the body isn't a JSON object with a `creator_id`). **What this catches that
per-address limiting would miss:** several accounts submitting from behind
the same NAT or proxy (a classroom, an office, a VPN exit node) stay
independent instead of sharing one limit. **What it costs:** an attacker who
rotates `creator_id` on every request — exactly what the `attacks.csv` family
of this project's own attack set does — looks like a thousand different
callers and never trips the limit at all; `FLOOD01`–`FLOOD05` in the attack
run only meant anything *because* they deliberately shared one `creator_id`.
A real deployment would need a second signal (address, account age, device
fingerprint) layered on top to catch that rotation.

---

## What's Still Broken

- **Criterion 1 is still a miss.** 3 of 10 own-writing samples (and 2 of 3
  `false_positive` attacks) still score `ai`. Stage: signal one,
  `detector.model_signal`. Mechanism: short, plainly-worded declarative
  sentences are exactly what a small language model finds easiest to
  predict, so they read as low-perplexity/high-AI regardless of authorship —
  and signal one carries 0.45 of the combined score, more than enough to
  carry a plain paragraph past 0.65 on its own. I didn't fix this one: the
  real fix is recalibrating `DETECTOR_PERPLEXITY_MIDPOINT` against a real
  set of human-written samples, and I don't have enough labeled calibration
  text to do that without just guessing a new number that might overcorrect
  the other way.
- **The typo evasion (`EV01`) now succeeds outright.** Stage: signal two,
  `type_token_ratio`. Mechanism: each misspelling creates a token that
  doesn't repeat anywhere else in the text, so deliberately typo'd text gets
  *more* credit for vocabulary variety than the clean version it was copied
  from. I stopped here because the real fix — normalizing or spell-correcting
  before measuring vocabulary variety — is a new preprocessing step, not a
  one-line tuning change, and risks its own new blind spots (a genuine
  non-native-English writer's real misspellings would get the same boost).
- **The injection attack (`INJ01`) is handled only by accident.** Neither
  signal reads meaning, so appending an instruction sentence does nothing —
  which is correct here but only because nothing in this service parses
  natural-language instructions in the first place. A future signal that
  *did* read meaning (an LLM-based judge, say) would need an explicit defense
  against this that doesn't exist anywhere in this codebase yet.

**The trade I'd make if this ran for real:** I'd keep favoring fewer false
accusations over catching more AI text, even knowing it leaves the typo
evasion open — a wrongly-accused writer pays in reputation on a site where
reputation is the product, while a missed AI paragraph costs the site a
little moderation work it can absorb. The writers who disguise AI text with
typos are the ones who pay for that choice by getting through; the writers
who never gamed anything are the ones who'd have paid if I'd gone the other
way.


<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

## Capstone

**What This Extends**

This extends Provenance Guard, the system from projects/units 7 and 8 in
this course — the Flask service that scores submitted text for how likely
it is to be AI-written, logs every decision, and lets a writer appeal. What's
new this unit is a `POST /batch` route: submit several pieces of text in one
call instead of looping `/submit` yourself.

**The Shape**

Shape C — extend one capability. Out of scope: no new detection signal, no
change to the three existing signals' weights or thresholds, no change to
`/submit`, `/appeal`, `/verify`, or rate limiting, and no attempt at Path A
hosting — `RUNNING.md` already worked out, with the memory arithmetic, that
the local GPT-2 detector rules that out regardless of how many routes the
service has.

> **Revised after the capstone writeup:** `RUNNING.md`'s arithmetic (torch +
> GPT-2 weights against a 512MB cap) is correct for the PaaS-style free
> tier it was measured against, but that's a property of *that host's*
> memory limit, not of every free host. Hugging Face Spaces' free CPU tier
> gives 16GB, which fits. See **Running It** below for whether Path A
> actually went live.
>
> **Why revised:** the original line treated "no free host fits" as a fact
> about the model, when it's really a fact about one specific host's
> ceiling. That's not a target I missed — it's a claim narrower than it
> was written.

**Running It**

Path B — local, with logs. Same command as every unit before this one:
`python app.py`, documented in [RUNNING.md](RUNNING.md). Nothing new to
install; `/batch` is just another route on the same process.

**Path A, attempted:** `Dockerfile` targets Hugging Face Spaces' free CPU
tier (SDK "Docker"), running `gunicorn app:app --preload` instead of
Flask's dev server, per `RUNNING.md`'s own instructions for running this
somewhere else. `--preload` imports `app.py` in gunicorn's master process
before forking workers, which skips `app.py::main()` entirely — so the
startup warm-up from "A Second Improvement" above is gated behind
`AI201_PRELOAD_WARMUP=1` (set in the `Dockerfile`) so it still runs there.
Smoke-tested locally under `gunicorn --preload`: first request after
startup measured **102.9ms**, not the ~7.9s cold start — confirming the
warm-up works the same way under a real WSGI server as it does under
`python app.py`.
<!-- TODO once deployed: replace this line with the live URL and one
    pasted curl against it, or say here that the Space build failed and
    why, instead of deleting this section. -->

**Instrumentation**

Every `/batch` item writes the same nine-plus-field entry `/submit` always
has (`timestamp`, `content_id`, `creator_id`, `guess`, `model_score`,
`style_score`, `combined_score`, `lexical_score`, `label`, `status`,
`verified_human`), plus `duration_ms` (wall time of the three signals +
scoring, timed with `time.perf_counter()` in `app.py::_score_and_log`) and
`batch_id` (shared by every item from one `/batch` call, plus an `index`,
so a batch's items can be found together).

A rejected item or request logs through `audit.log_rejection` with a
`reason` instead of a decision — `app.py::batch`'s own validation, and
`run_batch_eval.py`'s deliberately malformed scenarios, are what produced
the rejections below. **Every rejection now carries `duration_ms` too**
(time from the top of the route to the reject, passed through `_reject`'s
new `started` parameter): an earlier pasted log had this on the three
`decided` rows only, which hid that a rejection takes measurable time as
well — usually near-zero, but a number, not an absence. The
`DetectorUnavailable` branch in `/batch` (and in `/submit`) also now calls
`audit.log_rejection` before answering; it didn't before, which meant that
one specific failure mode showed up in the HTTP response but never in the
log — exactly the "failure that shows up only as an absence" this
project's own comments warn about elsewhere.

Ten real entries from `logs/audit.jsonl`, pasted as-is (three decided, then
seven rejected — including the two kinds of failed request this unit's
testing produced):

```json
{"timestamp": "2026-11-15T23:45:08+00:00", "content_id": "9481f99b-8cab-4e15-a9da-2121517c6af8", "creator_id": "batcheval_5", "guess": "unsure", "model_score": 0.6169, "style_score": 0.3783, "combined_score": 0.5901, "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you — if you wrote it yourself, you're welcome to appeal so a person can take a closer look.", "status": "decided", "lexical_score": 0.9005, "verified_human": false, "duration_ms": 87.9, "model_ms": 87.3, "style_ms": 0.3, "lexical_ms": 0.0, "scoring_ms": 0.1, "batch_id": "926291c0-c0a5-414c-a049-29d09eb96cca", "index": 4}
{"timestamp": "2026-11-15T23:45:08+00:00", "content_id": "f6454430-e5b6-408c-aee0-a193316b0843", "creator_id": "batcheval_6", "guess": "unsure", "model_score": 0.416, "style_score": 0.5735, "combined_score": 0.5542, "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you — if you wrote it yourself, you're welcome to appeal so a person can take a closer look.", "status": "decided", "lexical_score": 0.8316, "verified_human": false, "duration_ms": 79.9, "model_ms": 78.9, "style_ms": 0.4, "lexical_ms": 0.4, "scoring_ms": 0.1, "batch_id": "926291c0-c0a5-414c-a049-29d09eb96cca", "index": 5}
{"timestamp": "2026-11-15T23:45:09+00:00", "content_id": "88de0737-f86f-4d74-870b-fe4b7f2c31ec", "creator_id": "batcheval_7", "guess": "unsure", "model_score": 0.3859, "style_score": 0.5833, "combined_score": 0.5318, "label": "We can't tell confidently whether a person or an AI wrote this. That's not a strike against you — if you wrote it yourself, you're welcome to appeal so a person can take a closer look.", "status": "decided", "lexical_score": 0.7699, "verified_human": false, "duration_ms": 98.1, "model_ms": 97.8, "style_ms": 0.1, "lexical_ms": 0.0, "scoring_ms": 0.1, "batch_id": "926291c0-c0a5-414c-a049-29d09eb96cca", "index": 6}
{"timestamp": "2026-11-15T23:45:09+00:00", "creator_id": "batcheval_bad_1", "event": "rejected", "status": "rejected", "reason": "bad_request", "message": "'text' is required and must be a non-empty string.", "batch_id": "926291c0-c0a5-414c-a049-29d09eb96cca", "index": 7, "duration_ms": 0.0}
{"timestamp": "2026-11-15T23:45:09+00:00", "creator_id": "batcheval_bad_2", "event": "rejected", "status": "rejected", "reason": "bad_request", "message": "'text' is required and must be a non-empty string.", "batch_id": "926291c0-c0a5-414c-a049-29d09eb96cca", "index": 8, "duration_ms": 0.0}
{"timestamp": "2026-11-15T23:45:09+00:00", "creator_id": "batcheval_bad_3", "event": "rejected", "status": "rejected", "reason": "bad_request", "message": "'text' is required and must be a non-empty string.", "batch_id": "926291c0-c0a5-414c-a049-29d09eb96cca", "index": 9, "duration_ms": 0.0}
{"timestamp": "2026-11-15T23:45:09+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "bad_request", "message": "Batch of 30 items exceeds the 20-item limit.", "duration_ms": 0.1}
{"timestamp": "2026-11-15T23:45:09+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "bad_batch_item", "message": "Item must be a JSON object.", "batch_id": "17661b33-a457-460a-bded-e7ce71c4e63d", "index": 0, "duration_ms": 0.0}
{"timestamp": "2026-11-15T23:45:09+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "bad_request", "message": "'items' is required and must be a non-empty JSON array.", "duration_ms": 0.0}
{"timestamp": "2026-11-15T23:45:09+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "bad_request", "message": "'items' is required and must be a non-empty JSON array.", "duration_ms": 0.0}
```

**Latency breakdown (stretch).** The three decided rows above also carry
`model_ms`, `style_ms`, `lexical_ms` and `scoring_ms` — each signal timed on
its own inside `_score_and_log`, added this pass specifically to answer
"which stage actually costs the money." Across the 1,087 `decided` entries
in the current `logs/audit.jsonl`: `model_ms` median **52.7ms**, mean
64.5ms; `style_ms`, `lexical_ms` and `scoring_ms` are each a **median of
0.0ms**, meaning the two cheaper signals and the combining step together
account for well under 1% of a submission's cost. The entire per-item
latency story in this project is signal one, the model forward pass —
signal two and three are effectively free by comparison. That also means
the 20%-overhead bound in criterion 4 is really a bound on how much Flask
request/response handling and JSON work add on top of one GPT-2 forward
pass, not on anything the style or lexical signals do.

**What It Costs**

No API spend — the detector is a local GPT-2, so the only cost is compute
time on this machine. Measured, not estimated: 161 real `decided` log
entries (excluding the one-time ~7.6s model-load entry recorded before the
warm-up fix below) average **50.9 ms per submission**
(`duration_ms`, read back from `logs/audit.jsonl`). A `/batch` item costs
about the same per item as a solo `/submit` — see criterion 4 below.

**The hundred-a-day arithmetic:** 100 submissions/day × 0.0509s ≈ **5.1
seconds of compute/day** — trivially cheap in CPU-seconds. The real cost
this system carries isn't per-request compute, it's standing memory:
torch + the GPT-2 weights sit resident at roughly 0.75–1.3GB for as long
as the process runs, which is the number `RUNNING.md` already used to rule
out a free host. Batching doesn't change that arithmetic — it changes the
number of HTTP round trips, not the number of model calls.

**Run Log and Verdicts**

Three trials each, before and after the fix below. "Target" is a
per-trial bound — 20% over that trial's own solo per-item time, since the
solo baseline itself drifts slightly run to run; the other four criteria
are pass/fail as written in `criteria.md`. All five criteria's raw output
for every trial lives in the two files named below, not only criterion 4's
— the JSON blocks hold keys `1_and_4`, `2`, `3` and `5`, one per criterion,
inside each trial.

*Before* (`results/batch_run_2026-11-11_2203_before.md`):

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Batch correctness | 10/10 match, 3/3 trials | 10/10 | 10/10 | 10/10 | MET |
| 2. Partial-failure isolation | 7 decided + 3 errors, 0×500 | 7/3 | 7/3 | 7/3 | MET |
| 3. Batch size cap | 400, nothing processed | 400 | 400 | 400 | MET |
| 4. Batching overhead ≤20% | per-trial bound | 814.8 vs 63.7 | 50.6 vs 63.2 | 46.5 vs 55.4 | **MISSED** |
| 5. Malformed batch shapes (revised) | 400/400 | 400/400 | 400/400 | 400/400 | MET |

(An earlier version of this table had trial 1's numbers sitting in the
Target column and no entry at all for trial 3 — a transcription error, not
a second run. The numbers above are read directly back out of the three
JSON blocks in the file: trial 1 came in at 814.8ms/item against a 63.7ms
target — a 1,180% overage; trials 2 and 3 were already fine at 50.6ms
against 63.2ms and 46.5ms against 55.4ms. The target has to hold across
all three trials, so this is a miss.)

*After* (`results/batch_run_2026-11-11_2205_after.md`):

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Batch correctness | 10/10 match, 3/3 trials | 10/10 | 10/10 | 10/10 | MET |
| 2. Partial-failure isolation | 7 decided + 3 errors, 0×500 | 7/3 | 7/3 | 7/3 | MET |
| 3. Batch size cap | 400, nothing processed | 400 | 400 | 400 | MET |
| 4. Batching overhead ≤20% | per-trial bound | 53.0 vs 64.5 | 51.9 vs 64.4 | 54.9 vs 59.6 | **MET** |
| 5. Malformed batch shapes (revised) | 400/400 | 400/400 | 400/400 | 400/400 | MET |

*Re-check, after the logging and startup-warm-up fixes below*
(`results/batch_run_2026-11-15_1845_recheck.md`) — same five criteria, run
again once the audit-log gaps and the real cold-start fix (not just the
test harness's own warm-up call) were in place, to confirm neither changed
any verdict:

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Batch correctness | 10/10 match, 3/3 trials | 10/10 | 10/10 | 10/10 | MET |
| 2. Partial-failure isolation | 7 decided + 3 errors, 0×500 | 7/3 | 7/3 | 7/3 | MET |
| 3. Batch size cap | 400, nothing processed | 400 | 400 | 400 | MET |
| 4. Batching overhead ≤20% | per-trial bound | 68.9 vs 84.5 | 61.4 vs 74.0 | 59.3 vs 74.0 | **MET** |
| 5. Malformed batch shapes (revised) | 400/400 | 400/400 | 400/400 | 400/400 | MET |

Real output, trial 1 of the before run, criterion 4 (pasted from
`results/batch_run_2026-11-11_2203_before.md`):

```json
{
  "batch": {"status": 200, "elapsed_ms": 8148.0},
  "solo_per_item_ms": 53.1,
  "batch_per_item_ms": 814.8
}
```

**The Improvement**

**Diagnosis:** `detector.py::_load` lazily loads the ~550MB GPT-2 model on
the *first* call to `model_signal`, anywhere in the process, and keeps it
in memory after that. `run_batch_eval.py`'s trial 1 called `/batch` before
any `/submit` call, so the one-time model-load cost landed entirely inside
the batch timing — making a 10-item batch look 15x slower per item than it
actually is. Trials 2 and 3 were already fine because the model was warm
by then. The mechanism is a test-harness ordering problem, not a bug in
`/batch` itself: whichever call goes first absorbs the cold start, and in
this design that happened to always be the batch call.

**Fix:** added one warm-up `/submit` call at the top of
`run_batch_eval.py::main`, before any trial starts timing
(`run_batch_eval.py`, ~8 lines). Re-ran with `--label after`: all three
trials of criterion 4 now land within the 20% bound (table above). No
other criterion changed.

**A Second Improvement**

**Diagnosis:** the fix above only changed how the *test* measured the
system — `run_batch_eval.py` warms the model before timing starts, but
`app.py` itself still lazily loads the model on whichever real HTTP
request happens to arrive first. A real caller, not a test harness, would
be the one who pays the ~7.6s cold start. This is exactly the gap this
unit's own grading feedback named: "ask yourself whether a fix changes the
system or only how you observe it." It didn't, yet.

**Fix:** `app.py::main` now calls `detector.warm_up()` once at startup,
before `app.run()` opens the port, so the model is loaded before any
caller can reach it (`app.py`, ~8 lines). `detector.py::warm_up` also
changed — it was only calling `_load()`, which loads the model weights but
never runs a forward pass, so the *next* real call still paid for
PyTorch's own first-call kernel/thread-pool init on top of the (already
loaded) weights. `warm_up()` now also runs one throwaway `perplexity(...)`
call, which is the actual code path a real submission takes.

**Measured, same machine, same model, nothing else running:**

| | First real `/submit` after a fresh start |
|---|---|
| Before (no startup warm-up) | **7,855.8 ms** |
| After (startup warm-up, `_load()` only) | 2,799.9 ms — weights loaded, forward pass still cold |
| After (startup warm-up + one forward pass) | **90.9 ms** |

The middle row is itself a finding: loading the weights is not the same
thing as being warm. Measuring `_load()`-only warm-up made that visible —
the forward-pass-shaped fix only showed up as necessary once the smaller
fix was tried and still left a 30x–60x gap over the ~50ms steady-state
cost. The cost moves, it doesn't disappear: the ~7.6s now happens once, in
the terminal running `python app.py`, before anyone can send it a request,
instead of landing on whichever caller is first in line.

**Load Observation**

Run: `run_load_eval.py` against a freshly started, freshly warmed server —
100 `/batch` calls of 10 items each, back to back, as fast as the client
could send them: **1,000 scored items**, ten times this project's own
"100 submissions/day" cost arithmetic above, in one continuous burst
instead of spread across a day
(`results/load_run_2026-11-15_1847.md`).

| | |
|---|---|
| Items/sec sustained | 17.5 |
| Per-item `duration_ms`, median | ~53ms — matches the single-request baseline |
| Per-item `duration_ms`, mean | 56.7ms |
| First-half mean vs second-half mean | 59.7ms vs 53.8ms — no upward drift |
| Max | 2,700.8ms — one item, 1 of 1,000 |

No degradation under sustained load: the first and second halves of the
burst average within 6ms of each other, so there's no memory growth or
thread contention building up over 1,000 items. There is one real
anomaly worth naming rather than hiding: item 1 of the burst spiked to
2,700.8ms — all of it in `model_ms`, confirmed in `logs/audit.jsonl`
(`model_ms: 2699.9` on that entry) — on an otherwise fully warmed server,
with every other item in the run under 120ms. **I don't have a diagnosis
for this one.** It isn't the cold-start bug above (the model was already
warm and had already been used for the recheck run earlier in this
session) and it isn't a drift pattern (nothing else in the burst was
slow). My best guess is OS-level scheduling jitter — something else on
this laptop briefly took the CPU — but I haven't confirmed that, and I'd
rather say so than invent a mechanism I didn't actually trace.

**What's Still Broken**

- The 20% overhead bound in criterion 4 is itself a fairly loose target —
  measured overhead after the fix is closer to 0–5%, not the 20% ceiling.
  If I tightened it, I'd set it to 10%.
- `/batch` has no rate limiting of its own. `/submit` is limited per
  `creator_id`; a caller can currently send unlimited `/batch` calls at
  `MAX_BATCH_ITEMS` each and get `MAX_BATCH_ITEMS`× the throughput of the
  rate limit on `/submit`. I noticed this while building the route and
  decided it was out of scope — it's a real gap, and the fix would be
  applying the same `@limiter.limit(...)` decorator to `/batch`, scaled by
  item count rather than request count.
- The one thing I'd do first if this ran for real: rate-limit `/batch` by
  item count, not request count — it's the gap that actually matters for a
  deployed version of this, and it's a small, well-understood change given
  the limiter is already wired up for `/submit`.

**How I Used AI**

Two specific moments, using Claude Code in this session:

1. Before writing any code, I asked it to look at all four prior AI201
   projects and recommend one to extend plus a shape (A/B/C). It read
   `RUNNING.md`'s existing Path A/B memory arithmetic and pointed out that
   shapes A and B were both already mostly covered by this project's unit
   7/8 work (the audit log, the run path, rate limiting, the attack set) —
   so Shape C, a genuinely new capability, was the only one with real room
   left. I adopted that instead of defaulting to "extend whatever."
2. When the first `/batch` run showed criterion 4 missing by ~15x, but
   only on trial 1, I asked it to find the actual stage and mechanism
   rather than just loosen the target. It traced the spike to
   `detector.py::_load`'s lazy, process-wide model load landing inside
   whichever call ran first — which happened to always be the batch call
   in the test order — and that's what the fix (warming up before timing)
   is targeted at.

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
