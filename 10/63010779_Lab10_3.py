class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self,sizeTable,MaxCollision):
        self.table = [None]*sizeTable
        self.MaxCollision = MaxCollision

    def display(self):
        for i in range(len(self.table)) :print("#"+str(i+1)+"	"+str(self.table[i]))
        print("---------------------------")

    def add(self,key,value):
        numIndex=self.findHashNum(key)
        if self.table[numIndex]==None: self.table[numIndex]=Data(key,value)
        else : 
            temp=numIndex
            for i in range(self.MaxCollision):
                if self.table[temp]==None: 
                    self.table[temp]=Data(key,value)
                    break
                print("collision number "+str(i+1)+" at "+str(temp)) 
                temp = (numIndex+((i+1)**2))% len(self.table)
                if i ==  self.MaxCollision-1 :print("Max of collisionChain")
        
    def findHashNum(self,arr):
        sum=0
        for i in arr : sum+=ord(i)
        return sum % len(self.table)
    
    def tableIsFull(self):
        for i in self.table:
            if i == None : return False
        return True
    
    def discard(self):
        for i in range(len(self.table)) : self.table[i]=None
            

inp = input(' ***** Fun with hashing *****\nEnter Input : ').split('/')
n, data = list(map(int, inp[0].split())), list(map(str, inp[1].split(",")))       
table=hash(n[0],n[1])
for i in data:
    if not table.tableIsFull():
        key,value=i.split(" ")
        table.add(key,value)
        table.display()
    else: 
        print("This table is full !!!!!!")
        table.discard()
        break