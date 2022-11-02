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
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
    def printTree2(self, node,num, level = 0):
        if node != None:
            self.printTree2(node.right,num, level + 1)
            if node.data>num: print('     ' * level, str(node.data*3))
            else: print('     ' * level, node)
            self.printTree2(node.left,num, level + 1)

T1 = BST()
txt,k = input('Enter Input : ').split("/")
inp = [int(i) for i in txt.split()]
root=Node(inp[0])
for i in inp:
    root = T1.insert(root,int(i))
T1.printTree(root)
print("--------------------------------------------------")
T1.printTree2(root,int(k))
