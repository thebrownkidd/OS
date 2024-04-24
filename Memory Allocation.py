# first fir, best fir and worst fir memory allocation usnig linked list like datastructure
class block:
    def __init__(self,address,size = 0):
        self.size = size
        self.address = address
        self.name = ""
        self.avail = True
        self.next = None
        self.prev = None
    def isavail(self):
        return self.avail
    def allot(self, name):
        # if req <= 0:
            # return False
        self.name = name
        self.avail = False
        # req -= self.size
        # if req > 0:
            # return True
        # else:
            # return False
    # def setsize(self, s):
    #     self.size = s
    def searchforfit(self,req):
        avail = 0
        ret = self
        while avail < req:
            if  self.avail is True:
                avail += self.size     
            else:
                avail = 0
                ret = self.next
            if self.next is None and avail< req:
                print("Not enough Memory")
                return None
        return ret

# Now we define blocks
bsize = int(input("Enter a positive number that is the size of a block: "))
tmemory = int(input("Enter the total memory available: "))
no_of_blocks = int(tmemory/bsize)
head = block(0,bsize)
temp = head
prev = temp
add = 0
for i in range(1,no_of_blocks):
    add += bsize
    temp.next = block(add,bsize)
    temp = temp.next
    temp.prev = prev
    prev = prev.next
const = head
nchunk = int(input("Enter the number of chunks in your memory: "))
cname = []
csize = []
cocc = []
for i in range(nchunk):
    cname.append(str(input("Enter the name of this chunk: ")))
    csize.append(int(input("Enter the size of this chunk: ")))
    cocc.append(str(input("Enter the occupancy of this chunk as O or NO: ")).lower())
    for j in range(int(csize[i]/bsize)):
        if cocc[i] == "o":
            const.allot(cname[i])
            const = const.next
        else:
            const.name = cname[i]
print("You have successfully constructed memory")
r = int(input("What is your requirement: "))
e = head
fit = []
while True:
    e = e.searchforfit(r)
    s = e
    eoc = e
    if e is None:
        r = int(input("Enter new requirement: "))
        continue
    for i in range(r/bsize):
        s = s.prev
    # s is the start of a chunk, e is end of allocated memory, eoc is end of chunk
    con = True
    while con:
        if eoc.next is not None:
            if eoc.next.isavail():
                eoc = eoc.next
            else:
                con = False
    size_of_chunk = s.address - eoc.address
    waste = size_of_chunk - r
    fit.append([s.name,r])
    e = eoc
    if eoc.next is None:
        break

print("First fit is " + fit[0])
low = fit[0][1]
lowpro = fit[0][0]
high = low
highpro = lowpro
for x in fit:
    if low > x[1]:
        low = x[1]
        lowpro = x[0]
    if high < x[1]:
        high = x[1]
        highpro = x[0]
print("Best worst is :" + highpro +","+ str(high))
print("Best fit is: "+ lowpro+ ","+ str(low))
