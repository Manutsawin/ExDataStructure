class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

def createLL(LL):
    head=None
    tail=None
    for data in LL:
        if head is None:
            p=Node(data)
            head=p
            tail=p
        else:
            q=tail
            p=Node(data)
            p.next=q.next
            q.next=p
            tail=p
    return head       

def printLL(head):
    s = ''
    while head != None :
        s += str(head) + ' '
        head = head.next
    return s

def SIZE(head):
    size=0
    while head != None : 
        size+=1
        head = head.next
    return size

def scarmble(head, b, r, size):
    numB = int(float(b)//(100/size))
    numR = int(float(r)//(100/size))
    #BottomUp
    temhHead=head
    t=head
    for i in range(size):
        if i==numB-1: 
            p=t
            t=t.next
            p.next=None
            continue
        if i==numB: head=t
        if i==size-1: t.next=temhHead
        t=t.next
    print("BottomUp {:.3f} % : ".format(float(b)),end="")
    print(printLL(head))
    #Riffle
    t=head
    for i in range(size):
        if i == numR-1: 
            temhHead=t.next
            t.next=None
            break
        t=t.next
    t=head
    s=""
    count=0
    c1=0
    while t!=None or temhHead!= None:
        if (count%2==0 or temhHead==None) and c1<numR:
            if count!=size-1: s+=t.value+" "
            else:s+=t.value
            t=t.next
            c1+=1
        else:
            if count!=size-1 : s+=temhHead.value+" "
            else: s+=temhHead.value
            temhHead=temhHead.next
        count+=1
    head = createLL(s.split(" "))
    print("Riffle {:.3f} % : ".format(float(r)),end="")
    print(printLL(head))
    #Deriffle
    s1=""
    s2=""
    count=0
    c1=0
    c2=0
    while head != None:
        if (count%2==0 and c1<numR) or c2>=size-numR:
            s1+=head.value+" "
            c1+=1
        else:
            if c2 != size-numR-1: s2+=head.value+" "
            else: s2+=head.value
            c2+=1
        count+=1
        head=head.next 
    head=createLL((s1+s2).split(" "))
    print("Deriffle {:.3f} % : ".format(float(r)),end="")
    print(printLL(head))
    #Debottomup
    temhHead=head
    t=head
    for i in range(size):
        if i==(size-numB)-1: 
            p=t
            t=t.next
            p.next=None
            continue
        if i==size-numB: head=t
        if i==size-1: t.next=temhHead
        t=t.next
    print("Debottomup {:.3f} % : ".format(float(b)),end="")
    print(printLL(head))
    return head
    

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split(" "))
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        h=scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        h=scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)