class LinkedList :  
    class Node :
        def __init__(self,data,next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
        
    def __init__(self):                
            self.dummy = self.Node(None,None)
            self.size = 0

    def __str__(self):
        s = 'link list : '
        p = self.dummy.next
        while p != None :
            if p.next==None: s+= str(p.data)
            else: s+= str(p.data) + '->'
            p = p.next
        return s

    def isEmpty(self) :
        return self.size == 0        

    def append(self,data) :
        return self.insert(self.size,data)
    
    def nodeAt(self,i) :
        p = self.dummy
        for j in range(-1,i) :
            p = p.next
        return p
    
    def insert(self, index, data):
        p = self.nodeAt(index-1)
        p.next = self.Node(data,p.next)
        self.size += 1
    
l1=LinkedList()
t=input("Enter Input : ").split(" ")
temp=""
for i in t : temp+=i
text=temp.split(",")
first=True
for i in text:
    if first:
        x=i
        for j in x:
            l1.append(j)
        first=False
    else:
        x,d=i.split(":")
        index=int(x)
        if index<0 or index>l1.size: print("Data cannot be added")
        else:
            l1.insert(index,d)
            print("index = "+str(index)+" and data = "+str(d))
    if not l1.isEmpty():print(l1)
    else : print("List is empty")
            
