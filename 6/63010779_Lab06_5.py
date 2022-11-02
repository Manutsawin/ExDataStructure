def staircase(n,x):
    s=""
    if n==0: return "Not Draw!"
    elif n>0 : 
        s+=draw1(n-1)
        s+=draw2(x)
        if n!=1: s+="\n"+staircase(n-1,x+1)
        return s  
    elif n<0 :
        s+=draw1(x-1)
        s+=draw2(n*-1)
        if n!=-1: s+="\n"+staircase(n+1,x+1)
        return s
    
def draw1(n):
    s=""
    if n>0 : s+="_"+draw1(n-1)
    return s 

def draw2(n):
    s=""
    if n>0 : s+="#"+draw2(n-1)
    return s 

print(staircase(int(input("Enter Input : ")),1))