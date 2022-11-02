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
    
    
    def delete(self,root, data):
 
       
        if root is None:
            print("Error! Not Found DATA")
            return root

        if data < root.data:
            root.left = self.delete(root.left, data)
            return root
        elif(data > root.data):
            root.right = self.delete(root.right, data)
            return root

        if root.left is None and root.right is None:
            return None

        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        succParent = root

        succ = root.right
    
        while succ.left != None:
            succParent = succ
            succ = succ.left
    
        if succParent != root:
            succParent.left = succ.right
        else:
            succParent.right = succ.right
    
        root.data = succ.data
    
        return root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
txt = input("Enter Input : ").split(",")

root=None
for i in txt:
    command = i.split(" ")
    if command[0]=='i': 
        print("insert",str(command[1]))
        root = T.insert(root,int(command[1]))
    elif command[0]=='d': 
        print("delete",str(command[1]))
        root = T.delete(root,int(command[1]))
    T.printTree(root)
