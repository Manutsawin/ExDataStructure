class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.value)

class hash:
    def __init__(self,sizeTable,MaxCollision,Threshold):
        self.table = [None]*sizeTable
        self.MaxCollision = MaxCollision
        self.Threshold =Threshold

    def display(self):
        for i in range(len(self.table)) :print("#"+str(i+1)+"	"+str(self.table[i]))
        print("----------------------------------------")

    def add(self,value):
        numIndex=int(value)%len(self.table)
        if self.overThreshold() :
            print("****** Data over threshold - Rehash !!! ******")
            self.rehashing()
            self.add(value)
        elif self.table[numIndex]==None: self.table[numIndex]=Data(value,value)
        else : 
            temp=numIndex
            for i in range(self.MaxCollision):
                if self.table[temp]==None: 
                    self.table[temp]=Data(value,value)
                    break
                print("collision number "+str(i+1)+" at "+str(temp)) 
                temp = (numIndex+((i+1)**2))% len(self.table)
                if i ==  self.MaxCollision-1 :
                    print("****** Max collision - Rehash !!! ******")
                    self.rehashing()
                    self.add(value)
        
    def rehashing(self):
        size = len(self.table)*2
        while not self.PrimeNum(size):
            size+=1
        tableTemp=self.table
        self.table=[None]*size
        for i in range (len(tableTemp)-1,-1,-1):
            if tableTemp[i] != None: self.add(tableTemp[i].value)
     
        
    def PrimeNum(self,num):
        for i in range(2,(num//2)+1) : 
            if num%i==0 : return False
        return True
    
    def overThreshold(self):
        count=1
        for i in self.table:
            if i != None : count+=1
        ans = count/len(self.table)*100
        if ans > self.Threshold : return True
        else : return False
    
            

inp = input(' ***** Rehashing *****\nEnter Input : ').split('/')
n, data = list(map(int, inp[0].split())), list(map(str, inp[1].split()))       
table=hash(n[0],n[1],n[2])
print("Initial Table :")
table.display()
for i in data:
    print("Add : "+i)
    table.add(i)
    table.display()
   