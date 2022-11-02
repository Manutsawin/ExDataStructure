class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self,root,data):
        if root is None:
            return Node(data)
        else:
            if root.data == data:
                return root
            elif root.data < data:
                root.right = self.insert(root.right,data)
            else:
                root.left = self.insert(root.left, data)
        return root
    
    def checkpos(self,root,data,height):
        
        if self.height(root)==height and data == root.data : return "Root"
        elif self.height(root)==0 and data == root.data : return "Leaf"
        elif data == root.data :
            return "Inner"
        else:
            txt1,txt2="",""
            if root.left!=None:txt1=self.checkpos(root.left,data,height)
            if root.right!=None:txt2=self.checkpos(root.right,data,height)
            return txt1+txt2

    def height(self,root):
        if root is None:
            return -1 
        leftAns = self.height(root.left)
        rightAns = self.height(root.right)
        return max(leftAns, rightAns) + 1
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
root=None
for i in range (1,len(inp)):
    root = T.insert(root,inp[i])
T.printTree(root)
if T.checkpos(root,inp[0],T.height(root))!="": print(T.checkpos(root,inp[0],T.height(root)))
else: print("Not exist")