# Automation Tank Simulator

This project simulates a water tank filling and draining process using Python.  
It demonstrates basic automation logic (fill, drain, alarms, cycle counting, operator controls) similar to what’s found in PLC/SCADA systems.

---

## Features
- Fill until 100% → stop
- Fill + drain cycle
- Cycle counter
- Operator chooses number of cycles
- Emergency STOP command
- Pause/Resume controls

---

## Project Structure
- `tank_monitor.py` → main program with all features
- `docs/test_plan.md` → test plan (coming soon)
- `docs/ladder_logic.png` → ladder logic diagram (coming soon)

---

## How to Run
Clone this repository and run:

```bash
python tank_monitor.py
