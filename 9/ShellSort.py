def shell (l,dIncrements):
    for inc in dIncrements:
        for i in range(inc,len(l)):
            iEle = l[i]
            for j in range(i,-1,-inc):
                if iEle<l[j-inc] and j>=inc:
                    l[j]=l[j-inc]
                else:
                    l[j]=iEle
                    break

lst=[10,11,1,13,2,6,4,12,5,8,7,9,3]
dIncrements=[5,3,1]
print(lst)
shell(lst,dIncrements)
print(lst)