def odd_even(arr, s,pos):
    num=0
    if pos =="Even":num=1
    if arr=="S":
        text=""
        for i in range(len(s)):
            if i%2==num: text=text+s[i]
        return text  
    else:
        lst=s.split(" ")
        newlst=[]
        for i in range(len(lst)):
            if i%2==num: newlst.append(lst[i])
        return newlst
arr,s,pos = input("*** Odd Even ***\nEnter Input : ").split(",")
print(odd_even(arr,s,pos))
