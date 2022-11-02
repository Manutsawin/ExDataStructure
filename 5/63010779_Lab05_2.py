class DoublyLinkedList :
    class Node :
        def __init__(self,data,prev = None,next = None) :
            self.data = data
            if prev is None :
                self.prev = None
            else :
                self.prev = prev
            if next is None :
                self.next = None
            else :
                self.next = next
        
    def __init__(self):                
            self.dummy = self.Node(None,None,None)
            self.dummy.next = self.dummy.prev = self.dummy
            self.size = 0
            
    def __str__(self):
        s = 'linked list : '
        p = self.dummy.next
        for i in range(self.size) :
            if i!=self.size-1:s += str(p.data) + '->'
            else:s += str(p.data)
            p = p.next
        return s
    
    def str_reverse(self):
        s='reverse : '
        p=self.dummy.prev
        for i in range(self.size) :
            if i!=self.size-1:s += str(p.data) + '->'
            else:s += str(p.data)
            p = p.prev
        return s

    def isEmpty(self) :
        return self.size == 0
    
    def nodeAt(self,i) :
        p = self.dummy
        for j in range(-1,i) :
            p = p.next
        return p

    def append(self,data) :
        self.insert(self.size,data)

    def insert(self, index, data):
        q = self.nodeAt(index)
        p = q.prev
        x = self.Node(data,p,q)
        p.next = q.prev = x
        self.size += 1

    def indexOf(self,data) :
        q = self.dummy.next
        for i in range(self.size) :
            if q.data == data :
                return i
            q = q.next
        return -1

    def remove(self, data): 
        index=self.indexOf(data)
        if index!=-1:
            q = self.nodeAt(index)
            p = q.prev
            x = q.next
            p.next = x
            x.prev = p
            self.size -= 1
        return index

lst = DoublyLinkedList()
t = input("Enter Input : ").split(",")
for i in t:
    txt=i.split(" ")
    text=""
    c=""
    for j in txt:
        if j!="" and c=="":c=j
        elif j!="" : text=j
        
    if c=="A": lst.append(text)
    elif c=="Ab":
        lst.insert(0,text)
    elif c=="I":
        index,data=text.split(":")
        if int(index)>=0 and int(index)<=lst.size:
            lst.insert(int(index),data)
            print("index = "+index+" and data = "+data)
        else:
            print("Data cannot be added")
    elif c=="R":
        index=lst.remove(text)
        if index!=-1:print("removed : "+text+" from index : "+str(index))
        else : print("Not Found!")
    print(lst)
    print(lst.str_reverse())