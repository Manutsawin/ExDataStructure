def selection(lst):
    for last in range(len(lst)-1,-1,-1):
        biggest = lst[0]
        biggest_i = 0
        for i in range(1,last+1):
            if lst[i]>biggest:
                biggest=lst[i]
                biggest_i = i
        lst[last],lst[biggest_i]=lst[biggest_i],lst[last]


lst=[6,9,8,5,4]
print(lst)
selection(lst)
print(lst)