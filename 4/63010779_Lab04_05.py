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
    
class Stack:
    def __init__(self,lst=None):
        if lst==None: self.items=[]
        else : self.items=lst
    
    def push(self,i):
        self.items.append(i)
    
    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items==[]
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[-1]

def Mirror(text,Que,stack):
    
    Exp=0
    S=Stack()
    lst=[]
    for i in text:lst.append(i)
    lst.reverse()
    plus=True
    while plus:
        plus=False
        i=0
        while i<len(lst):
            if i<len(lst)-2 and lst[i]==lst[i+1] and lst[i] == lst[i+2]:
                plus=True
                Exp+=1
                S.push(lst.pop(i))
                lst.pop(i)
                lst.pop(i)
                break
            i+=1
    lst.reverse()
    for i in lst :Que.enQueue(i)
    while not S.isEmpty():stack.push(S.pop())
    return Exp

def Normal(text,stack,item):
    
    Exp,fail=0,0
    lst=[]
    plus=True
    for i in text :lst.append(i)
    while plus:
        i=0
        plus=False
        while i<len(lst):  
            if i<len(lst)-2 and lst[i]==lst[i+1] and lst[i] == lst[i+2]:   
                if not item.isEmpty() and  lst[i]==item.peek():
                    item.pop()
                    lst.pop(i)
                    lst.pop(i)
                    fail+=1
                    plus=True
                    break
                elif not item.isEmpty() :
                    temp=[]
                    count=0
                    while len(lst)>0:
                        temp.append(lst.pop(0))
                        if count==i+1: temp.append(item.pop())
                        count+=1
                    while len(temp)>0:lst.append(temp.pop(0))
                    i+=2
                else:
                    lst.pop(i)
                    lst.pop(i)
                    lst.pop(i)
                    Exp+=1
                    plus=True
                    break
            
            i=i+1
    for i in lst: stack.push(i)
    return [Exp,fail]

stackItem=Stack()
mirrorQ=Queue()
NormalStack=Stack()
N,M = input("Enter Input (Normal, Mirror) : ").split(" ")
mirExp = Mirror(M,mirrorQ,stackItem)
ExpFail=Normal(N,NormalStack,stackItem)
print("NORMAL :\n"+str(NormalStack.size()))
if NormalStack.isEmpty():print("Empty",end="")
while not NormalStack.isEmpty():print(NormalStack.pop(),end="")
print("\n"+str(ExpFail[0])+" Explosive(s) ! ! ! (NORMAL)")
if ExpFail[1] > 0: print("Failed Interrupted "+str(ExpFail[1])+" Bomb(s)")
print("------------MIRROR------------")
print(": RORRIM\n"+str(mirrorQ.size()))
if mirrorQ.isEmpty():print("ytpmE",end="")
while not mirrorQ.isEmpty():print(mirrorQ.deQueue(),end="")
print("\n(RORRIM) ! ! ! (s)evisolpxE "+str(mirExp))