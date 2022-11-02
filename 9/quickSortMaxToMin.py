

def partition(arr, low, high):
        i = (low-1)         
        pivot = arr[high]  
        for j in range(low, high):
            if ordinalCompare(arr[j],pivot) :
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
        
def ordinalCompare(arr1,arr2):
    for i in range(len(arr1)):
        if len(arr2)>i:
            if ord(arr2[i])>ord(arr1[i]):
                return True
            elif ord(arr1[i])==ord(arr2[i]):continue
            else: return False
        else: return False
    return True
lst=["บอกรัก","บอกรัก2","ABC","ABD"]
# lst=[1,7,3,9,6,4,5,10]
print(lst)
quick(lst,0,len(lst)-1)
print(lst)