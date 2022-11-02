print(" *** Summation of each digit ***")
num = int(input("Enter a positive number : "))
sum=0
while num>10 :
    sum+=(num%10)
    num=int(num//10)
sum+=num
print("Summation of each digit =  "+str(sum))
