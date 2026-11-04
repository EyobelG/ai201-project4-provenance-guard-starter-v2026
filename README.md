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

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



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

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
