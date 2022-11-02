def insertMinHeap(h,i):
    insertEle=h[i]
    fi = (i-1)//2
    while i > 0 and insertEle < h[fi]:
        h[i]=h[fi]
        i = fi
        fi = (i-1)//2
    h[i] = insertEle

h = [13,14,16,20,21,19,68,65,26,32,31]
print(h)
for i in range(1,len(h)):
    insertMinHeap(h,i)
print(h)