class sjf:

    def __init__(self, name, arrival, burst,priority, waiting, turnround, q, ready):
        self.name = name
        self.arrival = arrival
        self.burst = burst
        self.waiting = waiting
        self.turnround = turnround
        self.priority = priority
        self.q = q
        self.ready = ready


    def TakeInput(self):
        self.name = raw_input('Enter Process name: ')
        self.arrival = raw_input("Enter Arrival Time: ")
        self.burst = raw_input("Enter Burst Time: ")
        self.priority = raw_input("Enter priority: ")
        print

    def displayProcess(self):
        print "Name : ", self.name, ", Arrival Time: ", self.arrival, ", Burst Time: ", self.burst

########################################################################
p_count = input('Enter the No. of process which you want to execute: ')
#p_count = 4
queue = [sjf('',0,0,0,0,0,0,0) for _ in range(p_count)]
temp_process = sjf('',0,0,0,0,0,0,0)
temp = 0
for i in range (p_count):
    queue[i].TakeInput()
    temp = queue[i].priority
    if(temp==0 or temp==1 or temp==2 or temp==3):
        queue[i].q = 1
    else :
        queue[i].q = 2 
    queue[i].ready = 0
i=0
clock = queue[0].burst
for y in range (p_count):
    count = y
    while count < p_count:
        if queue[count].arrival < clock:
            queue[count].ready = 1
        count += 1
    count = y
    while count < p_count - 1:
        j = count + 1
        while j < p_count:
            if queue[count].ready == 1 and queue[j].ready == 1:
                if queue[count].q == 2 and queue[j].q == 1:
                    temp_process = queue[count]
                    queue[count] = queue[j]
                    queue[j] = temp_process

                    print clock
            j += 1
        
        count += 1
    count = y
    while count < p_count - 1:
        j = count + 1
        while j < p_count:
            if queue[count].ready == 1 and queue[j].ready == 1:
                if queue[count].q == 1 and queue[j].q == 1:
                    if queue[count].burst > queue[j].burst:
                        temp_process = queue[count]
                        queue[count] = queue[j]
                        queue[j] = temp_process
                    else :
                        break
                        print clock
            j += 1
        count += 1
    print queue[y].name,"\t",clock,"\t" ,clock + queue[y].burst
    clock = clock + queue[y].burst
    count = y
    while count < p_count :
        if queue[count].ready == 1:
            queue[count].ready = 0
        count += 1



    
