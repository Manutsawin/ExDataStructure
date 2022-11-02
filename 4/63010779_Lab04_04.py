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

def displayQ(Q):
    le=Q.size()
    for i in range(le):
        x=Q.deQueue()
        Q.enQueue(x)
        print(x,end="")
        if i != le-1:print(", ",end="")

def displayA(Q):
    le=Q.size()
    for i in range(le):
        x=Q.deQueue()
        A,L=x.split(":")
        Q.enQueue(x)
        if int(A)==0:print("Eat",end=":")
        elif int(A)==1:print("Game",end=":")
        elif int(A)==2:print("Learn",end=":")
        elif int(A)==3:print("Movie",end=":")

        if int(L)==0:print("Res.",end="")
        elif int(L)==1:print("ClassR.",end="")
        elif int(L)==2:print("SuperM.",end="")
        elif int(L)==3:print("Home",end="")
        if i != le-1:print(", ",end="")

def score(Q1,Q2):
    le=Q1.size()
    score=0
    for i in range(le):
        x=Q1.deQueue()
        A1,L1=x.split(":")
        x=Q2.deQueue()
        A2,L2=x.split(":")
        if A1==A2 and L1==L2 : score+=4
        elif L1==L2 : score+=2
        elif A1==A2 : score+=1
        else: score-=5
    if score>=7:print("Yes! You're my love! : Score is "+str(score)+".")
    elif score>0:print("Umm.. It's complicated relationship! : Score is "+str(score)+".")
    else:print("No! We're just friends. : Score is "+str(score)+".")

        

MyQ=Queue()
YourQ=Queue()

text = input("Enter Input : ").split(",")
for i in text:
    M,Y=i.split(" ")
    MyQ.enQueue(M)
    YourQ.enQueue(Y)
print("My   Queue = ",end="")
displayQ(MyQ)
print("\nYour Queue = ",end="")
displayQ(YourQ)
print("\nMy   Activity:Location = ",end="")
displayA(MyQ)
print("\nYour Activity:Location = ",end="")
displayA(YourQ)
print()
score(MyQ,YourQ)