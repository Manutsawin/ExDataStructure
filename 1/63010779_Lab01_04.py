def num_grid(lst):
    for loop1  in range(5):
        for loop2 in range(5):
            count = 0
            if lst[loop1][loop2]!="#":
                    if loop1>0 and loop2>0 and lst[loop1-1][loop2-1]=="#": count+=1
                    if loop1>0 and lst[loop1-1][loop2]=="#": count+=1
                    if loop1>0 and loop2<4 and lst[loop1-1][loop2+1]=="#": count+=1
                    if loop2>0 and lst[loop1][loop2-1]=="#":count+=1
                    if loop2<4 and lst[loop1][loop2+1]=="#":count+=1
                    if loop1<4 and loop2>0 and lst[loop1+1][loop2-1]=="#":count+=1
                    if loop1<4 and lst[loop1+1][loop2]=="#": count+=1
                    if loop1<4 and loop2<4 and lst[loop1+1][loop2+1]=="#" :count+=1
                    lst[loop1][loop2] = str(count)
            if lst[loop1][loop2]=="#":
                    lst[loop1][loop2]="#"
    return lst
lst_input = []
print("*** Minesweeper ***")
input_list = input("Enter input(5x5) : ").split(",")
for e in input_list:
    lst_input.append([i for i in e.split()])
print("\n",*lst_input,sep="\n")
print("\n",*num_grid(lst_input),sep="\n")


