l = [e for e in input("Enter Input : ").split()]
if l[0] == "EX":
    Ans = "minHeap and maxHeap"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    def partition(arr, low, high):
        i = (low-1)         
        pivot = arr[high]  
        for j in range(low, high):
            if arr[j] <= pivot:
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)
  
    def quick(arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:
            pi = partition(arr, low, high)
            quick(arr, low, pi-1)
            quick(arr, pi+1, high)
  

    def Mdn(lst): 
        return (len(lst)+1)/2
        
    l=list(map(int, l))
    for i in range(len(l)):
        lst=[]
        for j in range(i+1):
           lst.append(l[j])       
        print("list = "+str(lst)+" : median = ",end="")
        quick(lst,0,len(lst)-1)
        if Mdn(lst)>int(Mdn(lst)) : 
            print("{:.1f}".format((lst[int(Mdn(lst))-1]+lst[int(Mdn(lst))])/2))
        else : print("{:.1f}".format(lst[int(Mdn(lst))-1]))

   