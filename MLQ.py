class MLQ:

    def __init__(self, name, priority, burst,waiting, turnround):
        self.name = name
        self.priority = priority
        self.burst = burst
        self.waiting = waiting
        self.turnround = turnround


    def TakeInput(self):
        self.name = raw_input('Enter Process name: ')
        self.burst = raw_input("Enter Burst Time: ")
        self.priority = raw_input("System/User Process (0/1) :")
        print

    def displayProcess(self):
        print "Name : ", self.name, ", Arrival Time: ", self.arrival, ", Burst Time: ", self.burst

########################################################################

p_count = input('Enter the No. of process which you want to execute: ')
#p_count = 4
queue = [MLQ('',0,0,0,0) for _ in range(p_count)]
for i in range (p_count):
    queue[i].TakeInput()

temp_process = MLQ('',0,0,0,0)
i = 0
while i < p_count:
    k = i + 1
    while k < p_count:
        if queue[i].priority > queue[k].priority:
            temp_process = queue[i]
            queue[i] = queue[k]
            queue[k] = temp_process
        k += 1
    i += 1
avg_waiting = queue[0].waiting = 0
avg_turnround = queue[0].turnround = queue[0].burst

i = 1
while i < p_count:
    queue[i].waiting = int(queue[i-1].waiting) + int(queue[i-1].burst)
    queue[i].turnround = int(queue[i-1].turnround) + int(queue[i].burst)
    avg_waiting = int(avg_waiting) + int(queue[i].waiting)
    avg_turnround = int(avg_turnround) + int(queue[i].turnround)
    i += 1
    
avg_waiting = float(avg_waiting)/float(p_count)
avg_turnround = float(avg_turnround)/float(p_count)

print("Process\t  Priority\t  Burst Time\t Waiting Time\t Turnround Time")

for i in range(p_count):
    print queue[i].name,"\t\t", queue[i].priority,"\t\t", queue[i].burst,"\t\t", queue[i].waiting, "\t\t",  queue[i].turnround
    print

print "Average Waiting Time = ",round(avg_waiting,2)
print "Average Turnround Time = ",round(avg_turnround,2)

