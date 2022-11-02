def mergeSort(arr):
    if len(arr) > 1:
  
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
  
        i = j = k = 0
        while i < len(L) and j < len(R):
            if ordinalCompare(L[i],R[j]) :
                print(" k=",str(k),"   "," i=",str(i))
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


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

arr1="ASD1"
arr2="ASD"


# lst=[5,3,6,1,2,7,8,4]
print(lst)
mergeSort(lst)
print(lst)