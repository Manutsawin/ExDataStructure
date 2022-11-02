def search(arr,num):
    for i in arr: 
        if int(i)>int(num) :
            return str(i)
    return "No First Greater Value"

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), list(map(int, inp[1].split()))
for i in k :  print(search(sorted(arr),i))