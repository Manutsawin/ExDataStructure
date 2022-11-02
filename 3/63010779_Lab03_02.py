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

def ManageStack(lst):
    stack= Stack()
    for loop in lst:
        lst2=loop.split(" ")
        if lst2[0]=="P":
            if stack.isEmpty():print(-1)
            else:print("Pop = "+str(stack.pop()))
        elif lst2[0]=="A": 
            stack.push(int(lst2[1]))
            print("Add = "+str(stack.peek()))
        elif lst2[0]=="D": Delete(stack,lst2[1])   
        elif lst2[0]=="LD": LD(stack,lst2[1])
        elif lst2[0]=="MD": MD(stack,lst2[1])  
    print("Value in Stack = "+str(stack.items))

def Delete(stack,num):
    temp=Stack()
    if stack.isEmpty():
        print(-1)
        return stack
    while stack.isEmpty()==False:
        if int(stack.peek())==int(num):
            stack.pop()
            print("Delete = "+str(num))
        else:temp.push(stack.pop())
    while temp.isEmpty()==False: stack.push(temp.pop())
    return stack

def LD(stack,num):
    if stack.isEmpty():
        print(-1)
        return stack
    temp=Stack()
    while stack.isEmpty()==False:
        if int(stack.peek())<int(num):  
            print("Delete = "+str(stack.peek())+" Because "+str(stack.peek())+" is less than "+str(num))
            stack.pop()
        else:temp.push(stack.pop())
    while temp.isEmpty()==False: stack.push(temp.pop())
    return stack

def MD(stack,num):
    if stack.isEmpty():
        print(-1)
        return stack
    temp=Stack()
    while stack.isEmpty()==False:
        if int(stack.peek())>int(num):  
            print("Delete = "+str(stack.peek())+" Because "+str(stack.peek())+" is more than "+str(num))
            stack.pop()
        else:temp.push(stack.pop())
    while temp.isEmpty()==False: stack.push(temp.pop())
    return stack


lst = input("Enter Input : ").split(",")
ManageStack(lst)
