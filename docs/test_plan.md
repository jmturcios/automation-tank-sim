# Tank Simulator — Test Plan

**System Under Test (SUT):** `tank_monitor.py`  
**Purpose:** Validate core automation logic (fill, drain, alarms), operator controls (STOP, PAUSE/RESUME), and cycle counting.

## Scope
- Normal operation: fill → full → drain → empty
- Operator control: STOP, PAUSE, RESUME, target cycles
- Boundary & negative inputs
