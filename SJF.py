class sjf:

    def __init__(self, name, arrival, burst, waiting, turnround):
        self.name = name
        self.arrival = arrival
        self.burst = burst
        self.waiting = waiting
        self.turnround = turnround

    def TakeInput(self):
        self.name = raw_input('Enter Process name: ')
        self.arrival = raw_input("Enter Arrival Time: ")
        self.burst = raw_input("Enter Burst Time: ")  
        print

    def displayProcess(self):
        print "Name : ", self.name, ", Arrival Time: ", self.arrival, ", Burst Time: ", self.burst

##########################################

p_count = input('Enter the No. of process which you want to execute: ')
queue = [sjf('',0,0,0,0) for _ in range(p_count)]
queue2 = [sjf('',0,0,0,0) for _ in range(p_count)]
for i in range(p_count):
    queue2[i].TakeInput()

from operator import attrgetter
queue2.sort(key = attrgetter('burst'))

temp = 0
i = 0
k = 0
j=1
while i<1000:
    temp = 0
    while j>0:
        if temp < len(queue2):
            if(i>=int(queue2[temp].arrival)):
                queue2[temp].waiting = i - int(queue2[temp].arrival)
                queue2[temp].turnround = int(queue2[temp].waiting) + int(queue2[temp].burst)
                i += int(queue2[temp].burst)
                queue[k]=queue2[temp]
                k += 1
                """for k in range(p_count):
                    if(queue[k].name == queue2[temp]):
                        queue[k] = queue2[temp]
                        break
                """
                queue2.pop(temp)
                break


            else:
                temp += 1
        else:
            i += 1
            break

#waitingTime = startTime - arrivalTime
#turnaroundTime = burstTime + waitingTime = finishTime- arrivalTime

print("Process\t  Arrival Time\t  Burst Time\t Waiting Time\t Turnround")

for i in range(p_count):
    print queue[i].name,"\t\t", queue[i].arrival,"\t\t", queue[i].burst,"\t\t", queue[i].waiting,"\t\t", queue[i].turnround
    print

total_waiting = 0
total_turnround = 0

for i in range(p_count):
    total_waiting += int(queue[i].waiting)
    total_turnround += int(queue[i].turnround)

avg_waiting = float(total_waiting)/float(p_count)
avg_turnround = float(total_turnround)/float(p_count)

print "Avreage Waiting Time = ",round(avg_waiting, 2)
print "Average Turnround Time = ",round(avg_turnround,2)
