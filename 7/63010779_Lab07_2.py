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
    
    def height(self,root):
        if root is None:
            return -1 
        leftAns = self.height(root.left)
        rightAns = self.height(root.right)
        return max(leftAns, rightAns) + 1


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
root=Node(inp[0])
for i in inp:
    root = T.insert(root,i)
print("Height of this tree is :",str(T.height(root)))