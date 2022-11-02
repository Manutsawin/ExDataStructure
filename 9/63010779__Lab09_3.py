def bubbleMinToMax(lst):
    for last in range(len(lst)-1,-1,-1):
        swaped=False
        for i in range(last):
            if lst[i]>lst[i+1]:
                lst[i],lst[i+1]=lst[i+1],lst[i]
                swaped=True
        if not swaped: break

def bubbleMaxToMin(lst):
    for last in range(len(lst)-1,-1,-1):
        swaped=False
        for i in range(last):
            if lst[i]<lst[i+1]:
                lst[i],lst[i+1]=lst[i+1],lst[i]
                swaped=True
        if not swaped: break

def duplicate(lst):
    temp=[]
    for i in lst: 
        if temp.count(i)==0: temp.append(i)
        else: return True
    return False

def somethingDROME(lst):
    minTomax=False
    maxTomin=False
    if lst.count(lst[0])==len(lst): return "Repdrome"
    temp=[]
    for i in lst: temp.append(i)
    bubbleMaxToMin(temp)
    if temp==lst: maxTomin = True
    temp=[]
    for i in lst: temp.append(i)
    bubbleMinToMax(temp)
    if temp==lst: minTomax = True
    if duplicate(lst): 
        if minTomax : return "Plaindrome"
        elif maxTomin : return "Nialpdrome"
        else : return "Nondrome"
    else:
        if minTomax : return "Metadrome"
        elif maxTomin : return "Katadrome"
        else : return "Nondrome"
    
inp = input("Enter Input : ")
lst=[]
for i in inp : lst.append(i)
print(somethingDROME(lst))
