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

## Detailed Test Procedures

### T01 — Fill to Full
1. Run the program.
2. When prompted, enter `1` for cycles.
**Expected:** Tank level increases step-by-step (10, 20 … 100). At 100, prints overflow alarm and switches to draining.
**Evidence:**  
![T01 Evidence](docs/evidence/Screenshot%202025-09-08%20093839.png)


---

### T02 — Drain to Empty
1. Continue running after T01 without stopping.
**Expected:** Tank decreases step-by-step (90, 80 … 0). At 0, prints "Tank Empty" and restarts filling (or stops if cycle count is reached).
**Evidence:**  
![T02 Evidence](docs/evidence/Screenshot%202025-09-08%20094320.png)


---

### T03 — Fixed Cycle Count
1. Run the program.
2. Enter `2` when prompted for cycles.
**Expected:** The system completes exactly two full cycles (fill + drain) then shuts down with a message: "System shutting down after 2 cycles."
**Evidence:**  
![T03 Evidence](docs/evidence/<your-screenshot-file>.png)


---

### T04 — STOP During Fill
1. Run the program.
2. Enter `5` when prompted for cycles.
3. While tank is filling (e.g., 30–60%), type `STOP`.
**Expected:** Program shuts down immediately with "Emergency Stop pressed. Shutting down system."
**Evidence:**  
![T04 Evidence](docs/evidence/T04_stop.png)


---

### T05 — STOP During Drain
1. Run the program.
2. Enter `5` when prompted for cycles.
3. Wait until draining begins.
4. Type `STOP`.
**Expected:** Program shuts down immediately with "Emergency Stop pres

---

### T06 — PAUSE/RESUME
1. Run the program.
2. Enter `3` when prompted for cycles.
3. During fill or drain, type `PAUSE`.
4. Confirm tank level does not change while paused.
5. Type `RESUME`.
**Expected:** Program resumes from the same level and continues normal operation.
**Evidence:**  
![T06 Evidence](docs/evidence/T06_pause_resume.png)

## Test Execution Log

Use this table to record results as you run each case.  
Suggested statuses: **Pass / Fail / Blocked / Pending**.

| Date (YYYY-MM-DD) | Tester | Test ID | Status  | Notes / Evidence (timestamp lines, screenshots, commit hash) |
|-------------------|--------|---------|---------|---------------------------------------------------------------|
|                   |        | T01     |         |                                                               |
|                   |        | T02     |         |                                                               |
|                   |        | T03     |         |                                                               |
|                   |        | T04     |         |                                                               |
|                   |        | T05     |         |                                                               |
|                   |        | T06     |         |                                                               |
|                   |        | T07     |         |                                                               |
|                   |        | T08     |         |                                                               |
|                   |        | T09     |         |                                                               |
|                   |        | T10     |         |                                                               |

### Evidence Tips
- Copy short console snippets with timestamps (e.g., `12:03:15 Tank Filling: 100%`).
- If you add screenshots, place them in `docs/evidence/` and reference like: `docs/evidence/T03_run1.png`.
- If a bug is found, note the **expected vs actual** and the step where it occurred.


