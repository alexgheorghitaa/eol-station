# Documentation

Everything about the station: what it measures, how it is put together, and why each piece is
shaped the way it is. Fifteen chapters — you almost certainly do not want all of them, so the
[reading paths](#reading-paths) below say which four or five to pick.

The build guide that shows *how to wire it* is a separate thing. These pages describe **what
it does and why**, for someone evaluating the design rather than following it.

---

## Chapters

### Getting oriented

| | Chapter | What is in it |
|---|---|---|
| **01** | [Overview](01-overview.md) | What an EOL station is, the four questions this project answers, what is built versus specified, and the scope limits stated up front. |
| **02** | [Architecture](02-architecture.md) | The layers and the call graph, the shared connector pane convention, and a complete inventory of every VI with its state. |

### What is being measured

| | Chapter | What is in it |
|---|---|---|
| **03** | [The DUT simulator](03-dut-simulator.md) | The simulated pack: command set, reply grammar, the seed-driven fault model, the five reference units, and what the model deliberately does not do. |
| **04** | [Test specification](04-test-specification.md) | Where limits come from and why they live in a file. The order of operations and the reason for each position. The 3.50 V decision, documented rather than buried. |
| **06** | [The test steps](06-test-steps.md) | Insulation, cell OCV and spread, contactor and pack voltage — what each measures, returns and survives. The `ERR,` guard and the disaster it prevents. |

### How the station is built

| | Chapter | What is in it |
|---|---|---|
| **05** | [The instrument layer](05-instrument-layer.md) | `DUT_Query.vi`: one command in, one reply out, traced. Terminator ownership, refnum chaining, the trace schema and its one honest gap. |
| **07** | [The sequencer](07-sequencer.md) | The state machine: states, transitions, abort paths, and the error override. Why a state machine rather than a straight sequence. |
| **08** | [The verdict model](08-verdict-model.md) | Three outcomes, never two. Where the DUT-fault / tester-fault line is enforced, the `Result` type field by field, and first-failure attribution. |
| **13** | [LabVIEW design notes](13-labview-design-notes.md) | For readers who do not use LabVIEW: dataflow, chaining versus branching, type definitions and their sharp edge, and what binary VIs mean for reviewing this repo. |

### What comes out of it

| | Chapter | What is in it |
|---|---|---|
| **09** | [Reporting and evidence](09-reporting.md) | Three artefacts and who reads each: the per-unit HTML report, `results.csv`, and the `trace.csv` command log. |
| **10** | [Batch metrics](10-batch-metrics.md) | The golden gate, first pass yield, tester availability, and the first-failure Pareto — each with its exact denominator and the reason for it. |
| **11** | [Cycle time and frame decoding](11-cycle-time.md) | 96 transactions versus one packed burst read, the frame format dissected, and why the improvement is measured against a kept reference path rather than asserted. |
| **12** | [Failure injection and root cause](12-failure-injection.md) | Breaking the station on purpose: two injections, what each should produce, and how to diagnose a batch from its files alone. |

### Reference

| | Chapter | What is in it |
|---|---|---|
| **14** | [Mapping to NI TestStand](14-teststand-mapping.md) | What this station builds by hand and what TestStand provides. Written from documentation, not from experience — and it says so. |
| — | [Glossary](glossary.md) | Test-engineering, battery, protocol and LabVIEW terms, plus the error codes that actually came up. |
| — | [Test specification (formal)](TEST_SPEC.md) | The signed-off-shaped document: steps, limits, verdict model, open points. |
| — | [Screenshot shot list](SHOTLIST.md) | Build scaffolding — what each figure must show and how to capture it. |

---

## Reading paths

**Evaluating the engineering** — [Architecture](02-architecture.md) →
[The sequencer](07-sequencer.md) → [The verdict model](08-verdict-model.md) →
[LabVIEW design notes](13-labview-design-notes.md). Those four carry the trade-offs.

**Assessing the test content** — [Test specification](04-test-specification.md) →
[The test steps](06-test-steps.md) → [The DUT simulator](03-dut-simulator.md).

**What a production line would get** — [Reporting and evidence](09-reporting.md) →
[Batch metrics](10-batch-metrics.md) → [Failure injection](12-failure-injection.md).

**In fifteen minutes** — [Overview](01-overview.md), then
[the verdict model](08-verdict-model.md). Those two contain the reasoning that everything else
is an implementation of.

---

## Conventions used in these pages

- A **pending** marker means the code is specified but not yet built, so no measured value is
  quoted. Every number that is not marked pending came from running the simulator or a VI that
  works. See the build state table in [the overview](01-overview.md).
- Diagrams under `img/` are drawn from the design. Where a page shows a LabVIEW panel or block
  diagram for a VI that is not yet built, it says so in the caption.
- Repository files are linked directly — [`limits.csv`](../data/limits.csv),
  [`dut_sim.py`](../simulator/dut_sim.py) — so any claim can be checked against the source.

**Scope, repeated because it qualifies everything:** the DUT is simulated, the limits are
representative rather than calibrated, no measurement system analysis has been performed, and
timing figures come from one developer machine over TCP loopback. What this demonstrates is
the structure of an EOL station and the reasoning behind it.
