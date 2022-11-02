class Node:
 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insertCompleteBST(root,index,lst):
    
    if root is None:
        root=Node(lst[index])
        if (2*index)+1<=len(lst)-1: 
            root.left = insertCompleteBST(root.left,(2*index)+1,lst)
        if (2*index)+2<=len(lst)-1: root.right = insertCompleteBST(root.right,(2*index)+2,lst)
        return root
    else:
        if (2*index)+1<=len(lst)-1: root.left = insertCompleteBST(root.left,(2*index)+1,lst)
        if (2*index)+2<=len(lst)-1: root.right = insertCompleteBST(root.right,(2*index)+2,lst)
        return root

def sumNode(root):
    sum=0
    sum=root.data 
    if root.left!=None:sum+= sumNode(root.left)
    if root.right!=None:sum+= sumNode(root.right)
    return sum
    
def cut(root):
    if root==None:return root
    elif root.left == None and root.right==None:
        return root
    else :
        root.left=cut(root.left)
        root.right=cut(root.right)
        if root.right==None or root.left.data<root.right.data :
            if  root.right==None:x=0
            else:x=root.right.data
            k=Node(root.left.data)
            left=Node(0)
            left.left=root.left.left
            left.right=root.left.right
            right=Node(x-root.left.data)
            if  root.right==None:right.right==None
            else:right.right=root.right.right
            if  root.right==None:right.left=None
            else:right.left=root.right.left
            k.left=left
            k.right=right
            return k
        elif root.left==None or root.left.data>=root.right.data :
            if  root.left==None:x=0
            else: x=root.left.data
            k=Node(root.right.data)
            left=Node(x-root.right.data)
            if  root.left==None: left.left=None
            else:left.left=root.left.left
            if  root.left==None: left.right=None
            else : left.right=root.left.right
            right=Node(0)
            right.right=root.right.right
            right.left=root.right.left
            k.left=left
            k.right=right
            return k
        return root

N,txt=input("Enter Input : ").split("/")
lst=[]
for i in range(int(N)//2):lst.append(0)
for i in txt.split(" "):lst.append(int(i))
if len(lst)!=int(N):print("Incorrect Input")
else:
    root=None
    root=insertCompleteBST(root,0,lst)
    root = cut(root)
    print(sumNode(root))