# Test specification — 96S battery pack EOL

**Station:** EOL-SIM-01  ·  **DUT:** simulated 96-cell pack, ~355 V nominal
**Spec version:** 0.1 (draft — limits are representative, not calibrated)

## Order of operations, and why

1. **ID & comms** — nothing else is meaningful if the unit cannot be identified.
2. **Insulation** — measured *before* any high-voltage step. A pack with degraded
   isolation must never have its contactors closed.
3. **Cell OCV** — per-cell window plus cell-to-cell spread.
4. **Contactor** — only reached if insulation passed.

## Steps

| # | Step | Command | Limit | Source of limit | On failure |
|---|------|---------|-------|-----------------|-----------|
| 1 | ID & comms | `*IDN?` | prefix `SIMU,BP96`, reply < 2 s | protocol definition | retry ×1, then TESTER ERROR |
| 2 | Insulation | `MEAS:ISO?` | >= 2.0 MOhm | limits.csv | ABORT sequence |
| 3 | Cell OCV | `MEAS:VOLT:CELL? n` x96 or `MEAS:CELL:BURST?` | 3.50-3.85 V each | limits.csv | continue; log worst cell |
| 3b | Cell spread | derived: max - min | <= 0.05 V | limits.csv | continue |
| 4 | Contactor | `SYS:CONT CLOSE` + `MEAS:VOLT:PACK?` | `OK`, pack within +/-1 V of sum of cells | limits.csv | ABORT remaining |

## Verdict model

Three outcomes, never two:

| Verdict | Meaning | Counts toward |
|---------|---------|---------------|
| PASS | every executed step within limits | FPY numerator |
| DUT FAIL | at least one limit violated | FPY denominator only |
| TESTER ERROR | comms timeout, refused connection, or protocol error after retry | availability, **excluded from FPY** |

A step that was skipped because of an abort is recorded as SKIPPED. It is never
recorded as PASS.

## Tester health

A golden unit (`SYS:GOLDEN`) with known values — all cells 3.7000 V, insulation
10.00 MOhm — is tested before every batch. A failure means the station is at
fault; the batch does not proceed.

## Metrics produced per batch

- **First pass yield** = units passing on first attempt / units started
- **First-failure Pareto** = count of units by the first step that failed
- **Tester availability** = 1 - (tester errors / units started)
- **Cycle time** = total sequence duration per unit, and per step

## Open points

- Limits require sign-off before they mean anything outside this simulation.
- DCIR and capacity tests are specified in the wider domain but not implemented here.
- No measurement-system analysis (gauge R&R) has been performed.
- The CellOCV low limit is 3.50 V, not the 3.55 V a cell datasheet would
  suggest. The simulator's OCV model is base = 3.0 + 1.2*soc with
  soc = 0.45 + (seed%21)/100 and cells at base +/- 0.02 V, so a healthy pack
  can produce cells as low as 3.5200 V. A 3.55 V limit therefore sits inside
  the healthy population and fails good units. The limit is relaxed to match
  the model, not the cell. On real hardware the limit comes from the cell
  spec and the model is discarded.