# Tank Simulator — Test Plan

**System Under Test (SUT):** `tank_monitor.py`  
**Purpose:** Validate core automation logic (fill, drain, alarms), operator controls (STOP, PAUSE/RESUME), and cycle counting.

## Scope
- Normal operation: fill → full → drain → empty
- Operator control: STOP, PAUSE, RESUME, target cycles
- Boundary & negative inputs

## Test Environment
- OS: Windows/macOS/Linux
- Python 3.x installed
- Run from repository root with:
```bash
python tank_monitor.py

## Pass/Fail Criteria
- **Pass:** Actual behavior matches Expected Results for each test.
- **Fail:** Any deviation or unhandled error/traceback.

## Test Matrix (Overview)

| ID  | Name                        | Input / Action                      | Expected Result |
|-----|-----------------------------|-------------------------------------|-----------------|
| T01 | Fill to Full                | Start system                        | Tank rises step-by-step to 100%; prints overflow alarm |
| T02 | Drain to Empty              | Let system continue after full      | Tank decreases step-by-step to 0%; prints "Tank Empty" |
| T03 | Fixed Cycle Count           | Enter `2` for cycles                | Runs exactly 2 full cycles then stops |
| T04 | STOP During Fill            | Type `STOP` while filling           | Immediate shutdown with STOP message |
| T05 | STOP During Drain           | Type `STOP` while draining          | Immediate shutdown with STOP message |
| T06 | PAUSE/RESUME                | Type `PAUSE`, then `RESUME`         | Holds level steady; resumes from same level |
| T07 | Non-Numeric / Negative Input| Enter `-1` or text instead of number| Rejects input or re-prompts (Pending if not yet implemented) |
| T08 | Zero Cycles                 | Enter `0`                           | No cycles run; program exits politely |
| T09 | Large Cycles Boundary       | Enter `5`                           | Completes 5 cycles; then stops |
| T10 | No Double Count at Empty    | Watch transitions at 0%             | Cycle increments once per drain, no duplicates |
