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
    
    def minValueNode(node):
        current = node
        while(current.left is not None):
            current = current.left
        return current
    
    def deleteNode(self,root, data):
 
        
        if root is None:
            return root

        if data < root.data:
            root.left = self.deleteNode(root.left, data)
    
        elif(data > root.data):
            root.right = self.deleteNode(root.right, data)
    
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
    
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.minValueNode(root.right)
            root.data= temp.data
            root.right = self.deleteNode(root.right, temp.data)
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
        root = T.deleteNode(root,int(command[1]))
    T.printTree(root)
