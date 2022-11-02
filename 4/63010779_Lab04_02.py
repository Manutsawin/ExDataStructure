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
        
minus=0
M=Queue()
cashier1=Queue()
cashier2=Queue()
text = input("Enter people : ")
for i in text: M.enQueue(i)

while not M.isEmpty():
    minus+=1
    if not cashier1.isEmpty() and minus%3==1:cashier1.deQueue()
    if not cashier2.isEmpty() and minus%2==0:cashier2.deQueue() 
    
    if cashier1.size()<5: cashier1.enQueue(M.deQueue())
    elif cashier2.size()<5: cashier2.enQueue(M.deQueue())
    print(str(minus),str(M.items),str(cashier1.items),str(cashier2.items))
