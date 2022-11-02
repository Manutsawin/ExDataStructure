
def bubbleSort(lst):
    for last in range(len(lst)-1,-1,-1):
        swaped=False
        for i in range(last):
            if lst[i]>lst[i+1]:
                lst[i],lst[i+1]=lst[i+1],lst[i]
                swaped=True
        if not swaped: break

def Sum(lst):
    sum=0
    for i in lst: 
        sum+=int(i)
    return sum

def Extract(lst,size,answer):
   haveSub=False
   state=[]
   compare=[]
   ans=[]
   dist=[]
   delta =len(lst)-size
   for i in range(size,0,-1):dist.append(i)
   for i in range(size) : state.append(i)
   for i in range(delta,len(lst)) : compare.append(i)
   current=0
   while 1:
       temp=[]
       for i in state: temp.append(lst[i])
       if len(temp)==size and temp!=ans: 
           if Sum(temp)==answer:
               haveSub=True
               print(temp)
           ans=[]
           for i in temp:ans.append(i)
       if state==compare:break
       if state[current]==compare[current]:
            if state[current-1]+dist[current-1]<len(lst):
                current=current-1
                state[current]=state[current]+1
                for i in range(current,size-1,+1): state[i+1]=state[i]+1
                if current==0:
                    for i in range(size-1): state[i+1]=state[0]+i+1
            continue
       if current<size-1 and state[current]<len(lst)-1: 
           current+=1
           continue
       if state[current]<len(lst)-1: 
           state[current]+=1
   return haveSub

def Subset(lst,answer):
    haveSub=False
    for i in range(len(lst)): 
        if not haveSub : haveSub=Extract(lst,i+1,int(answer))
        else :Extract(lst,i+1,int(answer))    
    if not  haveSub:print("No Subset")
      
txt1,txt2=input("Enter Input : ").split("/")
lst=[int(i) for i in txt2.split()]
bubbleSort(lst) 
Subset(lst,int(txt1))



