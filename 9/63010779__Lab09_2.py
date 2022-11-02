def bubbleSort(lst):
    
    def swap(lst,left,right):
        check=True
        if right<len(lst): 
            if lst[right]<0: 
                lst=swap(lst,left,right+1)
                check=False
            elif lst[left]<0: 
                lst=swap(lst,left+1,right)
                check=False
            elif left==right: 
                lst=swap(lst,left,right+1)
                check=False
            elif lst[left]>lst[right]:
                lst[left],lst[right]=lst[right],lst[left]
               
        if right<len(lst)-1: 
            if check: lst=swap(lst,left+1,right+1)
        return lst
        
    if len(lst)>1: 
        swap(lst,0,1)
        lst[0:-1]=bubbleSort(lst[0:-1])
    return lst

lst=[int(i) for i in input('Enter Input : ').split()]
for i in bubbleSort(lst) :print(str(i)+" ",end="")
