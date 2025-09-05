"""
I confirm that this submission is my own work and is consistent with the Queen's
regulations on Academic Integrity.
"""

def roundRobinScheduling(processes, quantum):
    """
    processes: list of [pid, burst]  (arrival assumed 0 for all as in the lab)
    quantum: positive int time slice
    """
    n = len(processes)

    # parallel arrays indexed by process position
    remBurstTimes = [p[1] for p in processes]  # remaining burst time
    waitingTime = [0] * n
    turnaroundTime = [0] * n
    completionTime = [0] * n

    timeNow = 0  # current "clock"
    order = []  # list of (pid, ranUnits) in execution order

    print("\n--- Scheduling Run --------------------------------------------")
    print("Process set with arrival = 0 for all:")

    for pid, burst in processes:
        print(f"-P{pid}: burst={burst}")  # one space offset from process id for readability

    print(f"Time quantum: {quantum}")
    print("----------------------------------------------------------------\n")

    # Round-Robin loop, keep looping while any process still has remaining work
    # simple pass over processes in order; since arrivals are all 0
    while any(remBurstTimes[i] > 0 for i in range(n)):

        for i in range(n):
            if remBurstTimes[i] <= 0:
                continue

            # decide how much to run in this slice
            if remBurstTimes[i] > quantum:
                ran = quantum
                remBurstTimes[i] -= quantum
                timeNow += quantum

            else:
                ran = remBurstTimes[i]
                timeNow += remBurstTimes[i]
                remBurstTimes[i] = 0
                completionTime[i] = timeNow  # record when it finished

            # record execution for order + print the line for visibility
            pid = processes[i][0]
            order.append((pid, ran))
            print(f"- Ran P{pid} for {ran} unit(s)  (t = {timeNow})")

    # post-processing: arrival=0 for all, so
    # turnaround = completion - arrival => completion time
    # waiting = turnaround - burst
    for i in range(n):
        turnaroundTime[i] = completionTime[i]
        waitingTime[i] = turnaroundTime[i] - processes[i][1]

    # averages
    avgWaiting = sum(waitingTime) / n if n > 0 else 0.0
    avgTurnaround = sum(turnaroundTime) / n if n > 0 else 0.0

    # compute context switches accurately:
    # count transitions where consecutive slices change PID
    contextSwitches = 0
    for k in range(1, len(order)):
        if order[k][0] != order[k - 1][0]:
            contextSwitches += 1

    # --- Summary table  ---
    print("\nSummary per process:")
    print("Process ID\tBurst\tWaiting\tTurnaround\tCompletion")

    for i in range(n):
        print(f"P{processes[i][0]}\t\t{processes[i][1]}\t{waitingTime[i]}\t{turnaroundTime[i]}\t\t{completionTime[i]}")

    print(f"\nAverages:")
    print(f" --Average waiting time   : {avgWaiting:.2f}")  # two spaces offset from process id for readability
    print(f" --Average turnaround time: {avgTurnaround:.2f}")

    # execution order + context switches
    print("\nExecution order (in slices):")
    for index, (pid, ranUnits) in enumerate(order, start=1):
        print(f" {index}. P{pid} for {ranUnits} unit(s)")
    print(f"\nContext switches (PID changes between slices): {contextSwitches}")
    print("----------------------------------------------------------------\n")


if __name__ == "__main__":
    # fixed set like the lab (all arrival times = 0)
    processes = [[1, 10], [2, 1], [3, 2], [4, 1], [5, 5]]

    while True:
        # ask for a valid quantum
        stringInput = input("Enter time quantum (positive integer): ").strip()
        try:
            quantum = int(stringInput)
            if quantum <= 0:
                print("Time quantum must be positive.\n")
                continue
        except ValueError:
            print("Please enter a valid integer.\n")
            continue

        print(f"\n=== Running Round Robin with Time Quantum = {quantum} ===")
        roundRobinScheduling(processes, quantum)

        # ask to continue with a different quantum
        while True:
            cont = input("Run again with a different quantum? (Y/N): ").strip().upper() # ensures consistent user input
            if cont in ("Y", "YES"):
                print("") # blank line for readability
                break
            if cont in ("N", "NO"):
                print("Exiting...")
                raise SystemExit
            print("Please enter Y or N.")