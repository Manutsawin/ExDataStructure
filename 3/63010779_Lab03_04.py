class Stack:
    def __init__(self,lst=None):
        if lst==None: self.items=[]
        else : self.items=lst
    
    def push(self,i):
        self.items.append(i)
    
    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items==[]
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[-1]

class calculator:
    def __init__(self):
        self.stack=Stack()
    
    def run(self,instructions):
        lst=instructions.split(" ")
        for i in lst:
           try:
               if type(int(i))==int:self.stack.push(i)
           except:
                if i =="+": self.stack.push(int(self.stack.pop())+int(self.stack.pop()))
                elif i=="-": self.stack.push(int(self.stack.pop())-int(self.stack.pop()))
                elif i=="*": self.stack.push(int(self.stack.pop())*int(self.stack.pop()))
                elif i=="/": self.stack.push(int(self.stack.pop())//int(self.stack.pop()))
                elif i=="DUP": self.stack.push(self.stack.peek())
                elif i=="POP": self.stack.pop()
                else :
                    self.stack.push("Invalid instruction: "+str(i)) 
                    break
    
    def getValue(self):
        if self.stack.isEmpty():
            return 0
        return str(self.stack.peek())

print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = calculator()
machine.run(arg)
print(machine.getValue())

