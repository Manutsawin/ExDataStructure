def insertion(lst):
    for i in range(1,len(lst)):
        iEle = lst[i]
        for j in range(i,-1,-1):
            if iEle<lst[j-1] and j>0:
                lst[j]=lst[j-1]
            else:
                lst[j]=iEle
                break

lst=[4,1,6,5,3,2]
print(lst)
insertion(lst)
print(lst)