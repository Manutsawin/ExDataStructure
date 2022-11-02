class Queue:
    def __init__(self):
       self.items = []
    
    def enQueue(self,i):
        self.items.append(i)
    
    def deQueue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return len(self.items)==0
    
    def size(self):
        return len(self.items)

lst = input("Enter Input : ").split(",")
que=Queue()
for i in lst:
    x=i.split(" ")
    if x[0] =="E":
        print("Add "+x[1]+" index is "+str(que.size()))
        que.enQueue(x[1])
    elif  x[0] =="D":
        if not que.isEmpty(): print("Pop "+que.deQueue()+" size in queue is "+str(que.size()))
        else:print(-1)
if que.isEmpty():print("Empty")
else:print("Number in Queue is :  "+str(que.items))