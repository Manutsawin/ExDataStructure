class LinkedList :     
    class Node :                    
        def __init__(self, data, next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
        
    def __init__(self):                
            self.head = None
            self.size = 0
            
    def __str__(self):                
        s = ''
        p = self.head
        while p != None :
            if p.next !=None: s += str(p.data) + '->'
            else: s += str(p.data)
            p = p.next
        if s=='': return "Empty"
        return s
                  
    def __len__(self) :               
        return self.size

    def isEmpty(self) :               
        return self.size == 0
            
    def nodeAt(self,i) :              
        p = self.head
        for j in range(0,i) :
            p = p.next
        return p
    
    def insertAfter(self,i,data) :       
        q = self.nodeAt(i)
        p = self.Node(data)
        p.next = q.next
        q.next = p
        self.size += 1
    
    def append(self,data):            
        if self.head is None :
          p = self.Node(data)
          self.head = p
          self.size += 1
        else :                       
          self.insertAfter(len(self)-1,data)   
    
    def set_next(seft,index1,index2):
        node1=seft.nodeAt(int(index1))
        node2=seft.nodeAt(int(index2))
        node1.next=node2
        if int(index2)>int(index1): seft.size-=int(index2)-int(index1)-1
        print("Set node.next complete!, index:value = "+index1+":"+node1.data+" -> "+index2+":"+node2.data)
    
def findloop(txt,lst):
    loop = False
    for i in txt:
        x,y=i.split(" ")
        if x=="A":
            lst.append(y)
            print(lst)  
        elif x=="S":
            index1,index2=y.split(":")
            if int(index1)>=lst.__len__() or int(index1)<0:
                if int(index1)==0:
                    print("Error! {list is empty}")
                else: 
                    print("Error! {index not in length}: "+index1) 
            elif  int(index2)>=lst.__len__() or int(index2)<0 :
                lst.append(index2)
                print("index not in length, append : "+index2)
            else:
                lst.set_next(index1,index2)
                if int(index1)>=int(index2):
                    print("Found Loop") 
                    loop=True
                    break
    if not loop : print("No Loop\n"+str(lst))
                
lst = LinkedList()
txt=input("Enter input : ").split(",")  
findloop(txt,lst)          
           
    