class sjf:

    def __init__(self, name, arrival, burst,waiting, turnround, remain):
        self.name = name
        self.arrival = arrival
        self.burst = burst
        self.waiting = waiting
        self.remain = remain
        self.turnround = turnround


    def TakeInput(self):
        self.name = raw_input('Enter Process name: ')
        self.arrival = raw_input("Enter Arrival Time: ")
        self.burst = raw_input("Enter Burst Time: ")
        self.remain = self.burst
        print

    def displayProcess(self):
        print "Name : ", self.name, ", Arrival Time: ", self.arrival, ", Burst Time: ", self.burst

########################################################################

p_count = input('Enter the No. of process which you want to execute: ')
#p_count = 4
queue = [sjf('',0,0,0,0,0) for _ in range(p_count)]

for i in range (p_count):
    queue[i].TakeInput()
"""
queue[0].name = "p1"
queue[0].arrival = 0
queue[0].burst = 9

queue[1].name = "p2"
queue[1].arrival = 1
queue[1].burst = 5

queue[2].name = "p3"
queue[2].arrival = 2
queue[2].burst = 3

queue[3].name = "p4"
queue[3].arrival = 3
queue[3].burst = 4

queue[4].name = "p5"
queue[4].arrival = 2
queue[4].burst = 2

queue[5].name = "p6"
queue[5].arrival = 6
queue[5].burst = 3
"""
for i in range(p_count):
    queue[i].remain = queue[i].burst
t_slice = input('Enter Quantim Time :')

from operator import attrgetter
queue.sort(key = attrgetter('arrival'))

flag = 0
clock = 0
count = 0
remain = p_count
while (remain != 0):
    if(clock >= int(queue[count].arrival)):
        
        if (int(queue[count].remain) <= t_slice) and (int(queue[count].remain)>0) and clock >= int(queue[count].arrival):
            clock += queue[count].remain
            queue[count].remain = 0
            flag = 1
        elif (int(queue[count].remain)>0) and clock >= int(queue[count].arrival):
            queue[count].remain = int( queue[count].remain) - t_slice
            clock += t_slice
        if (queue[count].remain==0) and flag == 1:
            remain -= 1
            queue[count].turnround = clock - int(queue[count].arrival)
            queue[count].waiting = clock - int(queue[count].arrival) - int(queue[count].burst)
            flag = 0
        if (count == p_count - 1):
            count = 0
        elif (int(queue[count+1].arrival) <= clock):
            count += 1
        else :
            count = 0
    else :
        clock += 1

    
print("Process\t  Arrival Time\t  Burst Time\t Waiting Time\t Turnround Time")

for i in range(p_count):
    print queue[i].name,"\t\t", queue[i].arrival,"\t\t", queue[i].burst,"\t\t", queue[i].waiting, "\t\t",  queue[i].turnround
    print

total_turnround = 0
total_waiting = 0
for i in range(p_count):
    total_turnround += int(queue[i].turnround)
    total_waiting += int(queue[i].waiting)

avg_turnround = float(total_turnround)/float(p_count)
avg_waiting = float(total_waiting)/float(p_count)

print "Average Waiting Time = ",round(avg_waiting,2)
print "Average Turnround Time = ",round(avg_turnround,2)
