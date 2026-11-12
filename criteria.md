# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. False positives on my own writing

Of 10 short passages I write myself (not copied, not pasted from anywhere),
at most 1 is labeled `high-confidence AI`.

**Why this target:** On a writing site, calling a real writer's work AI is the
expensive mistake — it costs a person their credibility over something they
didn't do. Missing some AI-generated text costs the site a little moderation
work. A 1-in-10 ceiling says the system should almost never make that
accusation against an ordinary human writer, even though it can't be zero.

---

## 2. Score spread between clearly-AI and clearly-human text

A paragraph I generate from an AI model and a paragraph I write myself, both
on the same topic and similar length, score at least 0.40 apart on the
combined 0–1 scale.

**Why this target:** If the two signals can't separate the easiest possible
case — the one with no disguise at all — then the system has nothing to say
about the harder cases either. 0.40 is large enough that the two land in
different thirds of the scale, not just on opposite sides of a single
threshold line.

---

## 3. Label coverage

Each of the three labels — `high-confidence human`, `unsure`, and
`high-confidence AI` — is produced by at least one real piece of text I submit
while testing.

**Why this target:** A label nobody can reach is a gap in the threshold math,
not a real part of the system. If I can't produce all three on purpose, a
writer could get stuck seeing one that never resolves to a clear answer
either way.

---

## 4. The appeal path always works

Of 5 appeals I submit against valid content IDs, 5 move that item's status to
`under_review` and 5 show up in `GET /log` on the very next read.

**Why this target:** The appeal endpoint is the only thing standing between a
wrong accusation and nothing at all. A path that works most of the time is a
path a falsely-accused writer can't rely on — this one has to be 5 for 5, not
"usually."

---

## 5. Bad input never crashes the service

Of 3 malformed `/submit` requests — missing `text`, empty `text`, and a
50,000-character `text` — all 3 return a `400` with a readable error message,
and 0 return a `500`.

**Why this target:** A crash on bad input looks like a bug report, not a
judgment about anyone's writing, and a service that falls over on the first
weird request isn't one a real site could run. "Never 500 on malformed input"
is the one number on this list that should be unconditional.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->

---

## Capstone criteria — Unit 9

Five more, written before the extension is tested, for the new `/batch`
endpoint (Shape C — extend one capability). Four of five are about the
extension itself.

### 1. Batch correctness

Of 10 items sent in one `/batch` call, all 10 produce a `guess` and `label`
that match what `/submit` returns for that same text sent alone, across all
3 trials.

**Why this target:** a batch endpoint that scores things differently than
the single-item path isn't a convenience, it's a second, undocumented
scoring system. Agreement has to be total, not "usually."

### 2. Partial-failure isolation

Of a 10-item batch where 3 items are malformed (missing `text`, empty
`text`, `text` that isn't a string), the response always contains 7 decided
results and 3 per-item errors, with 0 HTTP 500s, across all 3 trials.

**Why this target:** the whole point of a batch call is that one caller's
typo in item 6 of 10 shouldn't cost them the other 9. If one bad item can
sink the batch, batching is strictly worse than looping `/submit` yourself.

### 3. Batch size cap holds

A batch of more than `MAX_BATCH_ITEMS` items is rejected with a `400` and
zero items processed (nothing appears in the audit log as `decided` from
that call), across all 3 trials.

**Why this target:** an unbounded batch turns one HTTP request into an
unbounded amount of model inference — the cap is the only thing standing
between a normal caller and someone using `/batch` to flood the detector.

### 4. Batching doesn't cost more per item

Averaged over a 10-item batch, the per-item time is no more than 20% slower
than the per-item time of 10 separate `/submit` calls, measured across 3
trials.

**Why this target:** 20% leaves room for batch-only overhead (JSON parsing
a bigger body, building the results list) without hiding a real regression
— if batching were, say, 2x slower per item, it would mean the model is
being reloaded or something else expensive is happening per item instead
of once.

### 5. Malformed batch shapes never crash the service

Of 3 malformed `/batch` requests — a non-dict item inside `items`, `items`
that isn't a list, and an empty `items` list — all 3 return a `400` with a
readable message, and 0 return a `500`.

**Why this target:** same reasoning as criterion 5 in unit 7 — a crash on a
weird shape is a bug report about the service, not a judgment about
anyone's writing, and it's the one number here that should be
unconditional.

> **Revised in unit 9:** Of 2 malformed `/batch` requests — `items` that
> isn't a list, and an empty `items` list — both return a `400` with a
> readable message, and 0 return a `500`. A list whose *items contain* a
> non-dict entry is **not** one of these cases: it's covered by criterion 2
> instead, which deliberately treats one bad item as an isolated per-item
> error rather than a reason to fail the whole batch.
>
> **Why revised:** the original bundled two different failure classes under
> one target. A non-dict item inside an otherwise-valid `items` list isn't a
> malformed *request* — it's exactly the "one bad item among many"
> situation criterion 2 exists to isolate, and the running code does isolate
> it (200, with a per-item `error` entry), which is correct given criterion
> 2's own design. The original target of "400" for that case was never
> reachable without breaking criterion 2, so it wasn't a criterion I missed
> — it was one that contradicted another criterion I'd already written.
