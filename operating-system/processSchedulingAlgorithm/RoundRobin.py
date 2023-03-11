import math
process = ["A", "B", "C"]
ArrivalTime = [0.00, 0.01, 0.02]
BurstTime = [9, 18, 12]
TimeQuantum = 5
total_process = len(process)
FinishTime = [0 for _ in range(total_process)]
pointer_time = 0

i = 0
TimeCount = [x for x in BurstTime]

while sum(TimeCount) != 0:
    if TimeCount[i] != 0:
        if TimeCount[i] < TimeQuantum and TimeCount[i] >= 0:
            pointer_time += TimeCount[i]
            TimeCount[i] = 0
            FinishTime[i] = pointer_time
        else:
            TimeCount[i] -= TimeQuantum
            pointer_time += TimeQuantum

    i += 1
    i %= total_process

TurnAroundTime = [FinishTime[i] -
                  math.floor(ArrivalTime[i]) for i in range(total_process)]
WaitingTime = [TurnAroundTime[i] - BurstTime[i] for i in range(total_process)]

print("FinishTime: ", FinishTime, "AV = ", sum(FinishTime) / total_process)
print("TurnAroundTime: ", TurnAroundTime,
      "AV = ", sum(TurnAroundTime) / total_process)
print("WaitingTime: ", WaitingTime, "AV = ", sum(WaitingTime) / total_process)
