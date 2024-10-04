#      1
#   2      3
# 4   5  6   7
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insert_recursively(self.root, data)
    
    def insert_recursively(self, node, data):
        if not node.left:
            node.left = Node(data)
        elif not node.right:
            node.right = Node(data)
        elif self.calc_height(node.left) <= self.calc_height(node.right):
            self.insert_recursively(node.left, data)
        else:
            self.insert_recursively(node.right, data)
    
    def calc_height(self, node):
        if not node:
            return 0
        return 1 + self.calc_height(node.left) + self.calc_height(node.right)
    
    def preorder(self, node):
        if node:
            print(node.data, end=",")
            self.preorder(node.left)
            self.preorder(node.right)
    
    def inorder(self, node):
        if node:
            self.preorder(node.left)
            print(node.data, end=",")
            self.preorder(node.right)
    
    def postorder(self, node):
        if node:
            self.preorder(node.left)
            self.preorder(node.right)
            print(node.data, end=",")

if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)
    
    print("Preorder", end=":")
    tree.preorder(tree.root)
    print("\nInorder", end=":")
    tree.inorder(tree.root)
    print("\nPostorder", end=":")
    tree.postorder(tree.root)
