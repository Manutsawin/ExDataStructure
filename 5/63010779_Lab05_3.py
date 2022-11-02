class node:
    def __init__(self,data,next = None ):
        self.data = data
        if next is None :
            self.next = None
        else :
                self.next = next
    def __str__(self):
        return str(self.data)

def createList(l=[]):
    size=0
    head=None
    tail=None
    for data in l:
        if head is None:
            p=node(data)
            head=p
            tail=p
            size+=1
        else:
            q=tail
            p=node(data)
            p.next=q.next
            q.next=p
            tail=p
            size+=1
    return head       

def printList(H):
    s = ''
    while H != None :
        s += str(H) + ' '
        H = H.next
    print(s)

def mergeOrderesList(p,q):
    s=""
    while p!=None or q!= None:
        if p==None:
            s+=str(q)+" "
            q=q.next
        elif q==None:
            s+=str(p)+" "
            p=p.next
        else :
            if int(p.data)<int(q.data):
                s+=str(p)+" "
                p=p.next
            else:
                s+=str(q)+" "
                q=q.next
    txt=s.split(" ")
    return createList(txt)

lst1,lst2 = input("Enter 2 Lists : ").split(" ")
L1=lst1.split(",")
L2=lst2.split(",")
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)
