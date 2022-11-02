def Binary(num,max,exp,check):
    if check<0:
        print("Only Positive & Zero Number ! ! !")
        return 0
    if num<max :
        if 2**exp>num:
            print("0",end="")
            if exp==0 : print()
            if exp>0 : Binary(num,max,exp-1,check)    
        else :
            print("1",end="")
            if exp==0 : print()
            if exp>0 : Binary(num-(2**exp),max,exp-1,check)
        if exp>check-2:Binary(num+1,max,exp,check)
num=int(input("Enter Number : "))
Binary(0,2**num,num-1,num)