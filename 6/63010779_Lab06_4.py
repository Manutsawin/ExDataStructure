def move(n,A,C,B,lst):
    if n == 1 :
        print("move",n, 'from ', A, 'to', C)
        changeLst(n,A,C,B,lst)
        displayLst(lst)
    else :
        lst=move(n-1,A,B,C,lst)
        print("move",n, 'from ', A, 'to', C)
        changeLst(n,A,C,B,lst)
        displayLst(lst)
        lst=move(n-1,B,C,A,lst)
    return lst

def displayLst(lst): 
    if len(lst[0])>0:
        print(lst[0][0]+"  "+lst[1][0]+"  "+lst[2][0])
        displayLst([lst[0][1:],lst[1][1:],lst[2][1:]])

def changeLst(n,A,C,B,lst):
    if A=='A':
        lst[0].remove(str(n))
        lst[0].insert(0,"|")
        if C=='B':
            length=len(lst[1])
            lst[1]=delCh(lst[1])
            lst[1].insert(0,str(n))
            lst[1]=addCh(length,lst[1])
        elif C=='C':
            length=len(lst[2])
            lst[2]=delCh(lst[2])
            lst[2].insert(0,str(n))
            lst[2]=addCh(length,lst[2])
    elif A=='B':
        lst[1].remove(str(n))
        lst[1].insert(0,"|")
        if C=='A':
            length=len(lst[0])
            lst[0]=delCh(lst[0])
            lst[0].insert(0,str(n))
            lst[0]=addCh(length,lst[0])
        elif C=='C':
            length=len(lst[2])
            lst[2]=delCh(lst[2])
            lst[2].insert(0,str(n))
            lst[2]=addCh(length,lst[2])
    elif A=='C':
        lst[2].remove(str(n))
        lst[2].insert(0,"|")
        if C=='A':
            length=len(lst[0])
            lst[0]=delCh(lst[0])
            lst[0].insert(0,str(n))
            lst[0]=addCh(length,lst[0])
        elif C=='B':
            length=len(lst[1])
            lst[1]=delCh(lst[1])
            lst[1].insert(0,str(n))
            lst[1]=addCh(length,lst[1])
    return lst

def addCh(num,lst):
    if len(lst)<num:
        lst.insert(0,"|")
        addCh(num,lst)
    return lst

def delCh(lst):
    if lst.count("|")>0:
        lst.remove("|")
        lst=delCh(lst)
    return lst

def creatLst(row,max,lst):
    if row<max: 
        lst.append(["|"])
        creatLst(row+1,max,lst)

def adddDfault(row,colum,max,lst):
    if row==1:
        if colum<max: 
            lst[row-1].append(str(colum))
            adddDfault(row,colum+1,max,lst)
            return 0
        else : adddDfault(row+1,1,max,lst)
    elif row<=3 :
        if colum<max: 
            lst[row-1].append("|")
            adddDfault(row,colum+1,max,lst)
            return 0
        else : adddDfault(row+1,1,max,lst)

n = int(input("Enter Input : "))
lst=[]
creatLst(0,3,lst)
adddDfault(1,1,n+1,lst)
displayLst(lst)
move(n,'A','C','B',lst)
