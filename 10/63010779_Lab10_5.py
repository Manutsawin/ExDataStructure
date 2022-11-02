def searchMinBox(data,numBox):
    weigth=0
    tempNumBox=numBox
    while True:
        sum=0
        for i in range(len(data)):
            if weigth<int(data[i]) or tempNumBox==0 :break
            sum+= int(data[i])
            if sum > weigth:
                if i == len(data)-1 and tempNumBox>1 and weigth+weigth>=sum :return weigth
                tempNumBox-=1
                sum=int(data[i])
                continue 
            if i == len(data)-1 : return weigth
        tempNumBox=numBox   
        weigth+=1
        
inp = input("Enter Input : ").split('/')
numBox=int(inp[1])
data = inp[0].split()
print("Minimum weigth for",str(numBox),"box(es) =",str(searchMinBox(data,numBox)))
