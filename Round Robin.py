# Simulate round robin scheduling algorythm

no_of_oprocesses = int(input("Please enter the number of processes: "))
readyq = []
for i in range(no_of_oprocesses):
    burst = int(input("enter the cou burst time of P"+str(i)+": "))
    name = 'P' + str(i)
    readyq.append([name,burst])
tq = int(input("Enter the time quantum: "))

comp = []
i = 0
t = 0
while len(readyq) != 0:
    # print(readyq, t,i)
    if i == len(readyq):
        i = 0
    readyq[i][1] -= tq
    print("\n",t)
    print(readyq[i][0])
    if readyq[i][1] <= 0:
        t += tq - readyq[i][1]
        comp.append([readyq.pop(i)[0],t])
    else:
        t += tq
        i += 1
    print(t)
print(comp)