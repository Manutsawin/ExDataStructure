def sum3Array(lst):
    if len(lst)<3: return "Array Input Length Must More Than "+str(len(lst))
    newlst=[]
    loop1,loop2,loop3=0,1,2
    while loop1<len(lst):
        while loop2<len(lst):
            while loop3<len(lst):
                if int(lst[loop1])+int(lst[loop2])+int(lst[loop3])==0:
                    if loop1!=loop2 and loop2!=loop3 and loop3 != loop1 and newlst.count([int(lst[loop1]),int(lst[loop2]),int(lst[loop3])])==0 : newlst.append([int(lst[loop1]),int(lst[loop2]),int(lst[loop3])])
                if loop3<len(lst): loop3+=1
            loop3=loop2+1
            if loop2<len(lst): loop2+=1
        loop2=loop1+1
        if loop1<len(lst): loop1+=1
    return newlst
lst = input("Enter Your List : ").split(" ")
print(sum3Array(lst))