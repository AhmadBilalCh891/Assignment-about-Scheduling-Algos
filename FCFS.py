class fcfs:
    #Count = 0

    def __init__(self, name, arrival, burst, waiting, turnround):
        self.name = name
        self.arrival = arrival
        self.burst = burst
        self.waiting = waiting
        self.turnround = turnround
        #fcfs.Count += 1

    def TakeInput(self):
        self.name = raw_input('Enter Process name: ')
        self.arrival = raw_input("Enter Arrival Time: ")
        self.burst = raw_input("Enter Burst Time: ")  
        print
        #fcfs.Count += 1

        
    def displayProcess(self):
        print "Name : ", self.name, ", Arrival Time: ", self.arrival, ", Burst Time: ", self.burst

##########################################

p_count = input('Enter the No. of process which you want to execute: ')
#p_count = 3
queue = [fcfs('',0,0,0,0) for _ in range(p_count)]

for i in range(p_count):
    queue[i].TakeInput()

from operator import attrgetter
queue.sort(key = attrgetter('arrival'))

temp = 0
i=0
while i<1000:
    if(i >= int(queue[temp].arrival) ):
        queue[temp].waiting = i - int(queue[temp].arrival)
        queue[temp].turnround = int(queue[temp].waiting) + int(queue[temp].burst)
        i += int(queue[temp].burst)
        temp += 1
        if(temp==p_count):
            break
    else:
        i = i+1


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
