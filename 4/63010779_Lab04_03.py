class Queue:
    def __init__(self,lst):
       if lst==[] :self.items = []
       else : 
           self.items = lst
    
    def enQueue(self,i):
        self.items.append(i)
    
    def deQueue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return len(self.items)==0
    
    def size(self):
        return len(self.items)


def encodemsg(q1,q2):
    le = q1.size()
    numtemp=Queue([])
    for i in range(q2.size()):
        x=q2.deQueue()
        numtemp.enQueue(x)
        q2.enQueue(x)
    for i in range(le):
        num=int(q2.deQueue())
        ch = q1.deQueue()
        if int(ord(ch))>96 and int(ord(ch))<123 and int(ord(ch))+num>122:
            x=int(ord(ch))+num-122
            q1.enQueue(chr(96+x))
        elif int(ord(ch))>64 and int(ord(ch))<91 and int(ord(ch))+num>90:
            x=int(ord(ch))+num-90
            q1.enQueue(chr(64+x))
        else:
            q1.enQueue(chr(int(ord(ch))+num))
        q2.enQueue(str(num))
    print("Encode message is :  "+str(q1.items))
    while not numtemp.isEmpty():
        q2.deQueue()
        q2.enQueue(numtemp.deQueue())


def decodemsg(q1,q2):
    le = q1.size()
    for i in range(le):
        num=int(q2.deQueue())
        ch = q1.deQueue()
        if int(ord(ch))>96 and int(ord(ch))<123 and int(ord(ch))-num<97:
            x=97-int(ord(ch))+num
            q1.enQueue(chr(123-x))
        elif int(ord(ch))>64 and int(ord(ch))<91 and int(ord(ch))-num<65:
            x=65-int(ord(ch))+num
            q1.enQueue(chr(91-x))
        else:
            q1.enQueue(chr(int(ord(ch))-num))
        q2.enQueue(str(num))
    print("Decode message is :  "+str(q1.items))

s,n = input("Enter String and Code : ").split(",")
string,number=[],[]
for i in s:
    if i != " ": string.append(i)
for i in n : number.append(i)
q1 = Queue(string)
q2 = Queue(number)

encodemsg(q1, q2)
decodemsg(q1, q2)