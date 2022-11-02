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

inp = input('Enter Infix : ')

S = Stack()

print('Postfix : ', end='')
### Enter Your Code Here ###
for i in inp:
    if (not S.isEmpty()) and S.peek()==")":
        S.pop()
        while not S.isEmpty():
            if S.peek()!="(":
                print(S.pop(),end="")
            else:
                S.pop()
                break
        S.push(i)
    elif (not S.isEmpty()) and S.peek()=="/":
        print(i+S.pop(),end="")
        while not S.isEmpty():
            if S.peek()=="+" or S.peek()=="+": print(S.pop(),end="")
            else:break
    elif (not S.isEmpty()) and S.peek()=="*":
        print(i+S.pop(),end="")
        while not S.isEmpty():
            if S.peek()=="+" or S.peek()=="+": print(S.pop(),end="")
            else:break
    elif i=="+" or i=="-" or i=="*" or i=="/" or i=="(" or i==")":
        S.push(i)
    else:
       print( i,end='')


while not S.isEmpty():

    print(S.pop(), end='')

print()