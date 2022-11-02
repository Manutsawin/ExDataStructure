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
            print("*")
            return Node(data)
        else:
            if root.data == data:
                return root
            elif root.data < data:
                print("R",end="")
                root.right = self.insert(root.right,data)
            else:
                print("L",end="")
                root.left = self.insert(root.left, data)
        return root
    
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
root=None
for i in inp:
    root = T.insert(root,i)
