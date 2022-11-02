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

def CheckVal(v1,v2):
    val1,val2=0,0
    lst=["+","-","*","/","^"]
    for i in range(len(lst)):
        if  v1==lst[i]:
            if i==1 or i==3 :val1=i-1
            else:val1=i
        if  v2==lst[i]:
            if i==1 or i==3 :val2=i-1
            else:val2=i
    return bool(val1>=val2)

inp = input('Enter Infix : ')
S = Stack()
print('Postfix : ', end='')
## Enter Your Code Here ###
for i in inp:
    
    if i==")":
        while not S.isEmpty():
            if S.peek()=="(":
                S.pop()
                break 
            else:print(S.pop(),end="")
    elif i=="(":
        S.push(i)
    elif i=="+" or i=="-" or i=="*" or i=="/" or i=="^":
        if not S.isEmpty() and CheckVal(S.peek(),i): 
            if i=="/" or i=="*":
                if S.peek()!="(":print(S.pop(),end="")
            else:
                if S.peek()!="(":print(S.pop(),end="")
                if not S.isEmpty() and S.peek()!="(":print(S.pop(),end="")
        S.push(i)      
    else:
       print( i,end='')

while not S.isEmpty():print(S.pop(), end='')
print()