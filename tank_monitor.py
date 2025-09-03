import time

# Ask the operator how many cycles to run
target_cycles = int(input("Enter number of cycles to run: "))

tank_level = 0
filling = True
cycles = 0
paused = False

while True:
    # Operator command check
    command = input("Press Enter to continue, 'PAUSE' to pause, or 'STOP' to shut down: ")
    
    if command.upper() == "STOP":
        print("🛑 Emergency Stop pressed. Shutting down system.")
        break
    
    elif command.upper() == "PAUSE":
        paused = True
        print("⏸️ System Paused. Type 'RESUME' to continue.")
        while paused:
            resume_cmd = input("Enter command: ")
            if resume_cmd.upper() == "RESUME":
                paused = False
                print("▶️ System Resumed.")
            elif resume_cmd.upper() == "STOP":
                print("🛑 Emergency Stop pressed. Shutting down system.")
                exit()

    # Normal operation
    if filling:
        tank_level += 10
        print(f"Tank Filling: {tank_level}%")
        if tank_level >= 100:
            print("🚨 Alarm: Tank Overflow! Starting drain...")
            filling = False
    else:
        tank_level -= 10
        print(f"Tank Draining: {tank_level}%")
        if tank_level <= 0:
            cycles += 1
            print(f"✅ Cycle {cycles} complete.")

            if cycles >= target_cycles:
                print(f"System shutting down after {target_cycles} cycles.")
                break

            filling = True

    time.sleep(1)
