# Mapping to NI TestStand

**Stated first, so nothing below can be read as more than it is: I have never used NI
TestStand.** This chapter is a model-level correspondence between what this station builds by
hand and what TestStand provides out of the box. It is written from documentation and from
building the equivalent structure myself, not from experience operating it.

That is worth writing down anyway, for two reasons. Building a step/sequence model by hand
forces you to meet the problems TestStand exists to solve, which is a better preparation than
having never thought about them. And it makes clear which parts of this repository are
*deliberate re-implementation* and which are simply absent.

**On this page:** [What TestStand is](#what-teststand-is) · [The mapping](#the-mapping) ·
[What this project deliberately mirrors](#what-this-project-deliberately-mirrors) ·
[What it does not attempt](#what-it-does-not-attempt) · [Would porting be worth it](#would-porting-this-be-worth-it)

## What TestStand is

TestStand is a **test executive**: the layer above your test code that decides what runs, in
what order, under what conditions, and what happens to the results.

The division of labour is the point. Your test code — a LabVIEW VI, a C DLL, a Python module —
measures one thing and returns a number. TestStand owns everything around it: sequencing,
limits and pass/fail evaluation, result collection, report generation, database logging,
operator interface, and the wrapper that identifies each unit and loops the whole thing.

The pieces referred to below:

| Concept | What it is |
|---|---|
| **Sequence file** | The test program: an ordered list of steps with their properties. |
| **Step type** | What a step *does*. Numeric Limit Test, Pass/Fail Test, String Value Test, Action, and others. A Numeric Limit Test knows it produces a number and compares it against bounds. |
| **Adapter** | How a step calls external code — LabVIEW, C/C++ DLL, .NET, Python. |
| **Process Model** | The wrapper around the test sequence: unit identification, looping, report generation, database logging. Sequential, Parallel and Batch models ship with it. |
| **Callbacks** | Defined hook points — before a unit, after a unit, on setup and cleanup — that you override without editing the model. |
| **Result collection** | Automatic. Every step contributes to a results list without the test code doing anything. |

## The mapping

| This project builds by hand | TestStand provides | Notes |
|---|---|---|
| `Sequencer.vi` — a While loop, a Case Structure, three shift registers | The **sequence file** and its execution engine | The hand-built version is one flat state machine. TestStand sequences nest, branch, loop and call subsequences. |
| `TestState.ctl` — an enum naming each step | Step identity in the sequence file | Here a state is a case in a structure; there it is a row in a table with properties. |
| The shared connector pane — `(connection, limits, error) → results` | **Adapter** parameter mapping | Mine is a hard convention I have to enforce myself. TestStand maps each step's parameters explicitly, so steps need no common signature. |
| `CheckLimit.vi` — value plus bounds, returns a typed verdict | **Numeric Limit Test** step type | The closest one-to-one correspondence in the project. |
| `Result.ctl` — 9 fields per row | The step's automatic result properties | Roughly the same fields, including limits, measurement and status. |
| `Load_Limits.vi` reading `limits.csv` | **Property Loader** step, reading limits from file or database | Same idea, same motivation: limits are data, not code. |
| `Report_Write.vi` — HTML per unit | Built-in report generation, HTML/XML/ATML | Mine writes one fixed layout. TestStand's is configurable and standards-based. |
| `Batch.vi` — golden gate then 30 units | **Process Model** — the Sequential model plus a `PreUUTLoop` callback | This is the largest single thing TestStand would replace. |
| The `results.csv` accumulation | Database logging | Mine is a CSV; TestStand ships schemas for real databases. |
| Passing the TCP refnum down the chain | A **Functional Global Variable** or a station global holding the session | The standard TestStand answer to "share one instrument session across steps". |
| `Run_One.vi` as an entry point | The operator interface | TestStand ships several; mine is a front panel. |

## What this project deliberately mirrors

Three design choices were made *because* they are how a test executive works, not because they
were the easiest way to get a measurement:

**A step returns a typed result, not a boolean.** Every row carries `value`, `low`, `high`, a
signed `margin`, a duration, a note and a status. That is close to what a TestStand Numeric
Limit Test records automatically, and it is what makes a report useful rather than merely
correct. See [the verdict model](08-verdict-model.md).

**Flow control lives at the sequence level, not inside the tests.** `Test_Iso.vi` reports that
insulation is out of limits. It does not decide that the sequence should abort — the `Iso` case
in the sequencer decides that, and marks the remaining steps `Skipped`. A test step that
controlled sequence flow could not be reordered or reused. See
[the sequencer](07-sequencer.md).

**Limits come from a spec file, resolved at run time.** Nothing is hard-coded in a step. This
is the Property Loader pattern, and it is the answer to the first question a test-engineering
interview asks. See [the test specification](04-test-specification.md).

The consequence of all three is that every case in the sequencer performs the same four moves —
unbundle, call, append results, choose the next state — so adding a fourth test is a new VI and
one more case rather than a redesign. That regularity is what a sequencer *is*.

## What it does not attempt

Listed so the correspondence is not mistaken for parity:

- **Parallel and Batch process models.** Testing several units simultaneously on one station,
  with synchronisation between them, is a substantial part of what TestStand does. This project
  tests one unit at a time.
- **A real operator interface.** TestStand ships operator UIs with login, lot tracking and
  serial entry. Mine is a LabVIEW front panel.
- **Database logging.** `results.csv` is a file.
- **Callbacks and model customisation.** There is no hook architecture here; the wrapper is
  code I edit directly.
- **Deployment.** TestStand has a deployment utility, licence tiers and a runtime story for
  getting a sequence onto a production machine. This is a repository you clone.
- **Step types beyond limit testing.** No message popups, no external executable calls, no
  synchronisation steps, no property loader step types.
- **ATML / standards-based reporting.** The report is bespoke HTML.

## Would porting this be worth it

Honestly assessed, since the question is obvious:

**What it would replace.** The sequencer, the report writer and the batch runner — roughly
sessions 5, 6 and 7 of the build. The three test VIs would survive unchanged; TestStand calls
LabVIEW VIs as steps, which is exactly what they are.

**What it would cost.** A licence — TestStand is not free, and the trial is time-limited —
plus learning a substantial tool well enough not to produce something worse than the hand-built
version.

**What it would prove.** Familiarity with the actual tool the job description asks for, which
the hand-built version cannot claim and this chapter is careful not to claim either.

**The honest position today:** the structure here is the right shape, and I can explain why
each piece of it exists. That is not the same as having run a sequence file in production, and
this chapter exists so that nobody has to work out the difference for themselves.

<!-- nav -->
---

| | | |
|:--|:-:|--:|
| ← [LabVIEW design notes](13-labview-design-notes.md) | [Documentation index](README.md) | [Glossary](glossary.md) → |
