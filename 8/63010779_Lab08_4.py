class Node:
 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root,data,lst):
    
    if root is None:
        root=Node(lst[data])
        if (2*data)+1<=len(lst)-1: 
            root.left = insert(root.left,(2*data)+1,lst)
        if (2*data)+2<=len(lst)-1: root.right = insert(root.right,(2*data)+2,lst)
        return root
    else:
        if (2*data)+1<=len(lst)-1: root.left = insert(root.left,(2*data)+1,lst)
        if (2*data)+2<=len(lst)-1: root.right = insert(root.right,(2*data)+2,lst)
        return root

def sumPower(root):
    sum=0
    sum=root.data 
    if root.left!=None:sum+= sumPower(root.left)
    if root.right!=None:sum+= sumPower(root.right)
    return sum
    
def compare(root1,root2):
    if sumPower(root1)>sumPower(root2):return">"
    elif sumPower(root1)<sumPower(root2):return"<"
    else:return"="

def sumLst(lst):
    sum=0
    for i in lst: sum+=i
    return sum

txt1,txt2=input("Enter Input : ").split("/")
lst=txt1.split(" ")
comp=txt2.split(",")
for i in range(len(lst)): lst[i]=int(lst[i])
lstNode=[None]*len(lst)
root=None
for i in range(len(lst)):
    root=insert(root,i,lst)
    lstNode[i]=insert(None,i,lst)
print(sumLst(lst))
for i in comp:
    x=i.split(" ")
    print(str(x[0])+compare(lstNode[int(x[0])],lstNode[int(x[1])])+str(x[1]))

