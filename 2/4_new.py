def sum3Array(lst):
    if len(lst)<3: return "Array Input Length Must More Than "+str(len(lst))
    newlst=[]
    for loop1 in range(len(lst)): 
        for loop2 in range(loop1+1,len(lst)): 
            for loop3 in range(loop2+1,len(lst)):
                if int(lst[loop1])+int(lst[loop2])+int(lst[loop3])==0: 
                    if newlst.count([int(lst[loop1]),int(lst[loop2]),int(lst[loop3])])==0 : newlst.append([int(lst[loop1]),int(lst[loop2]),int(lst[loop3])])
    return newlst
lst = input("Enter Your List : ").split(" ")
print(sum3Array(lst))
