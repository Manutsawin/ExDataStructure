def length(txt):  
    if txt=='' :
        return 0
    else: 
        sum=1+length(txt[0:-1])
        if sum%2==1: print(txt[-1]+"*",end="")
        else : print(txt[-1]+"~",end="")
    return sum
print("\n",length(input("Enter Input : ")),sep="")
