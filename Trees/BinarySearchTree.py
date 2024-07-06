class Node:
	def __init__(self, data):
		if not data:
			print("data could not be none")

		self.data = data
		self.left = None
		self.right = None
	
class BinarySearchTree:
	#		4
	#	2		6
	# 1	  3	  5     7
	def __init__(self):
		self.root = None
	
	def insert(self, data):
		if not self.root:
			self.root = Node(data)
		else:
			self.insert_recursively(self.root, data)
	
	def insert_recursively(self, node, data):
		if data < node.data:
			if not node.left:
				node.left = Node(data)
			else:
				self.insert_recursively(node.left, data)
		else:
			if not node.right:
				node.right = Node(data)
			else:
				self.insert_recursively(node.right, data)
	
	def traverse_preorder(self):
		self.traverse_preorder_recursively(self.root)

	def traverse_preorder_recursively(self, node):
		if not node:
			return None
		
		print(node.data, end=", ")
		self.traverse_preorder_recursively(node.left)
		self.traverse_preorder_recursively(node.right)
	
	def traverse_inorder(self):
		self.traverse_inorder_recursively(self.root)

	def traverse_inorder_recursively(self, node):
		if not node:
			return None
		
		self.traverse_inorder_recursively(node.left)
		print(node.data, end=", ")
		self.traverse_inorder_recursively(node.right)
	
	def traverse_postorder(self):
		self.traverse_postorder_recursively(self.root)

	def traverse_postorder_recursively(self, node):
		if not node:
			return None
		
		self.traverse_postorder_recursively(node.left)
		self.traverse_postorder_recursively(node.right)
		print(node.data, end=", ")

tree = BinarySearchTree()
# tree.insert(4)
# tree.insert(2)
# tree.insert(1)
# tree.insert(3)
# tree.insert(6)
# tree.insert(5)
# tree.insert(7)

tree.insert(15)
tree.insert(6)
tree.insert(23)
tree.insert(7)
tree.insert(72)
tree.insert(4)
tree.insert(50)
tree.insert(5)

print("Preorder", end=" - ")
tree.traverse_preorder()
print("\nInorder", end=" - ")
tree.traverse_inorder()
print("\nPostorder", end=" - ")
tree.traverse_postorder()