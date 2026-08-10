# Glossary

Terms used across this documentation, with the chapter that covers each properly.

## Test engineering

**Cycle time** — How long one unit takes. Measured here per step (`duration ms` on each
result row) and per unit (total sequence duration). → [Cycle time](11-cycle-time.md)

**DUT** — Device Under Test. The thing being measured. Here, a simulated 96-cell battery
pack. → [The DUT simulator](03-dut-simulator.md)

**DUT fail** — A verdict meaning the unit was measured and a limit was violated. Distinct from
a tester error, where no measurement happened. → [The verdict model](08-verdict-model.md)

**EOL** — End of line. The station at the end of a production line that gives a finished unit
its final pass/fail verdict. → [Overview](01-overview.md)

**First failure** — The first step in the sequence that a unit failed. Each reject is
attributed to exactly one, so the Pareto counts root causes rather than
symptoms. → [Batch metrics](10-batch-metrics.md)

**FPY — first pass yield** — Units passing on the first attempt, divided by units the station
actually managed to test. Tester errors are removed from the denominator, not counted as
failures. → [Batch metrics](10-batch-metrics.md#first-pass-yield)

**Gauge R&R / MSA** — Measurement system analysis: studies quantifying how much of the observed
variation comes from the measurement rather than the product. **None has been performed on this
project**, which is why no claim here depends on repeatability.

**Golden unit** — A reference unit whose correct answers are known exactly, tested before a
batch to verify the station itself. Here: `SYS:GOLDEN`, all 96 cells at 3.7000 V, insulation
10.00 MΩ. → [Batch metrics](10-batch-metrics.md#the-golden-gate)

**Margin** — The signed distance from a measured value to the nearest limit. Positive is
headroom; negative is how far out of limits the unit is. → [The test steps](06-test-steps.md#checklimitvi)

**Pareto** — A count of rejects grouped by cause, ordered by frequency, used to decide what to
fix first. → [Batch metrics](10-batch-metrics.md#the-first-failure-pareto)

**Skipped** — A step that did not run, usually because an earlier step aborted the sequence.
Recorded as `Skipped`, never as `Pass` and never as
`Fail`. → [The verdict model](08-verdict-model.md)

**Spec limit** — The bound a measurement is judged against. In this project every limit lives
in `data/limits.csv` with a `source` column naming its
provenance. → [Test specification](04-test-specification.md)

**Tester availability** — The fraction of presented units the station managed to test at all.
`1 − (tester errors ÷ units started)`. → [Batch metrics](10-batch-metrics.md#tester-availability)

**Tester error** — A verdict meaning the station failed to obtain a measurement: timeout,
refused connection, protocol error. Excluded from FPY, counted in
availability. → [Failure injection](12-failure-injection.md#error-taxonomy)

**UUT** — Unit Under Test. Interchangeable with DUT in this documentation.

## Battery and measurement

**96S** — Ninety-six cells in series. At roughly 3.7 V per cell that is about 355 V nominal.

**Cell spread (ΔV)** — The difference between the highest and lowest cell voltage in a pack. A
balance indicator. Limit here: 0.05 V. → [The test steps](06-test-steps.md#test_cellocvvi)

**Contactor** — The high-voltage switch that connects a pack's cells to its terminals. Closed
to measure pack voltage, and re-opened on every exit path including the error
path. → [The test steps](06-test-steps.md#test_contactorvi)

**DCIR** — Direct-current internal resistance. Part of a real pack EOL specification and
**not implemented here**.

**Insulation resistance** — Resistance between the high-voltage system and chassis. Measured
before anything is energised, because a pack with degraded isolation must never have its
contactors closed. → [Test specification](04-test-specification.md#order-of-operations)

**OCV** — Open-circuit voltage. A cell's voltage with no load, which is why it is measured
before the contactors close.

**Pack voltage** — Voltage at the pack terminals with the contactors closed. Cross-checked
against the sum of the 96 individual cell readings; agreement suggests both measurement paths
are trustworthy.

**SOC** — State of charge. In the simulator, derived from the seed and used to set each unit's
base cell voltage between 3.54 and 3.78 V. → [The DUT simulator](03-dut-simulator.md#what-it-models)

## Protocol and communications

**Big-endian** — Most significant byte first. The burst frames encode each cell as a
big-endian 16-bit millivolt value. → [Cycle time](11-cycle-time.md)

**CRLF** — Carriage return plus line feed, `\r\n`. The DUT's reply terminator, which is why the
station reads in CRLF mode.

**Framing** — Deciding where one message ends and the next begins in a byte stream. The DUT
splits requests on `\n` and terminates replies with `\r\n`.

**Refnum** — LabVIEW's handle to an open resource, here a TCP connection. Chained rather than
branched, so that the wire carries execution
order. → [LabVIEW design notes](13-labview-design-notes.md#chaining-versus-branching)

**SCPI** — Standard Commands for Programmable Instruments. A text command convention
(`MEAS:VOLT?`, `*IDN?`) that the simulator follows in
style. → [The DUT simulator](03-dut-simulator.md#protocol)

**Terminator** — The character sequence marking the end of a message. Owned exclusively by
`DUT_Query.vi`; sending it twice produces `ERR,SYNTAX`. → [The instrument layer](05-instrument-layer.md)

**`*IDN?`** — The SCPI identification query. Returns vendor, model, serial and firmware.

## LabVIEW

**Block diagram** — The code. Nodes connected by wires; execution order comes from data
dependency alone. → [LabVIEW design notes](13-labview-design-notes.md#dataflow-is-the-whole-language)

**Connector pane** — A VI's parameter list: which front-panel objects are inputs and outputs,
and in which position. All three test steps share
one. → [The test steps](06-test-steps.md#one-shape-three-steps)

**Control / indicator / constant** — A control is an input (a source; nothing can be wired
into it), an indicator is an output, a constant is a fixed value on the diagram. Which one you
get depends on where you drop the object.

**Dataflow** — The execution model: a node runs when all its inputs have data, and never
because of where it sits on the screen.

**Front panel** — A VI's user interface, and simultaneously its parameter declaration.

**Polymorphism** — Arithmetic nodes operating on arrays as readily as scalars, element by
element, with no loop. → [LabVIEW design notes](13-labview-design-notes.md#array-polymorphism)

**Quick Drop** — `Ctrl`+`Space`, then type a node's name to place it.

**Shift register** — A loop-border pair that carries a value from one iteration to the next.
The sequencer uses three: state, test data, error.

**subVI** — A VI called by another VI. Every file in `lib/` is one.

**Tunnel** — Where a wire crosses a structure's border. An **output** tunnel of a Case
Structure is shared by every case and must be wired in all of
them. → [LabVIEW design notes](13-labview-design-notes.md#case-structure-tunnels)

**Type definition (type def, `.ctl`)** — A file defining one data type. Instances stay linked
to it, so adding a field updates every copy at once — unless an instance has become
disconnected, which is silent and
costly. → [LabVIEW design notes](13-labview-design-notes.md#type-definitions-and-their-one-sharp-edge)

**VI** — Virtual Instrument, LabVIEW's unit of code. One file, a front panel and a block
diagram. Stored as **binary**, which is why they cannot be diffed or merged in
git. → [LabVIEW design notes](13-labview-design-notes.md#reviewing-a-labview-repository)

## Error codes seen in this project

| Code | Meaning | Usually |
|---|---|---|
| **1** | Invalid refnum or parameter | the connection was closed before it was used — an ordering bug |
| **56** | Timeout | something is listening but not answering; often an aborted VI holding the single client slot |
| **63** | Connection refused | nothing is listening — the simulator is not running |
| **66** | Peer closed the connection | the DUT process died mid-exchange |
| **84** | Format specifier does not match inputs | a `Format Into String` node edited by dragging rather than through its dialog |

→ [Failure injection](12-failure-injection.md#error-taxonomy)

<!-- nav -->
---

| | | |
|:--|:-:|--:|
| ← [Mapping to NI TestStand](14-teststand-mapping.md) | [Documentation index](README.md) | &nbsp; |
