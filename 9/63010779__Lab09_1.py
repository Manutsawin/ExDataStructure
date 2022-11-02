def bubbleSort(lst):
    
    def swap(lst,left,right):
        if lst[left]>lst[right]:
            lst[left],lst[right]=lst[right],lst[left]
        if right<len(lst)-1: 
            lst=swap(lst,left+1,right+1)
        return lst
        
    if len(lst)>1: 
        swap(lst,0,1)
        lst[0:-1]=bubbleSort(lst[0:-1])
    return lst

lst=[int(i) for i in input('Enter Input : ').split()]
print(bubbleSort(lst))
