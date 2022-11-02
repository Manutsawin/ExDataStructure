def Factorial(num):
    if num==0:return 1
    else: num=num*Factorial(num-1)
    return num
num = int(input("Enter Number : "))
print(str(num)+"! = "+str(Factorial(num)))