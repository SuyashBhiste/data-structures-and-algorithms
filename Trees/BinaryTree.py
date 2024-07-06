class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class BinaryTree:
	#		1
	#	2		3
	# 4	  5	  6     7
	def __init__(self):
		self.root = None
	
	def insert(self, data):
		if not self.root:
			self.root = Node(data)
		else:
			self.insert_recursively(self.root, data)

	def insert_recursively(self, current_node, data) -> bool:
		if current_node:
			if not current_node.left:
				current_node.left = Node(data)
				return True
			elif not current_node.right:
				current_node.right = Node(data)
				return True
			elif not self.insert_recursively(current_node.left, data):
					self.insert_recursively(current_node.right, data)
	
	def traverse_preorder(self):
		self.traverse_preorder_recursively(self.root)
	
	def traverse_preorder_recursively(self, current_node):
		if current_node:
			print(current_node.data, end=", ")
			self.traverse_preorder_recursively(current_node.left)
			self.traverse_preorder_recursively(current_node.right)
	
	def traverse_inorder(self):
		self.traverse_inorder_recursively(self.root)
	
	def traverse_inorder_recursively(self, current_node):
		if current_node:
			self.traverse_inorder_recursively(current_node.left)
			print(current_node.data, end=", ")
			self.traverse_inorder_recursively(current_node.right)
	
	def traverse_postorder(self):
		self.traverse_postorder_recursively(self.root)
	
	def traverse_postorder_recursively(self, current_node):
		if current_node:
			self.traverse_postorder_recursively(current_node.left)
			self.traverse_postorder_recursively(current_node.right)
			print(current_node.data, end=", ")

bt = BinaryTree()
bt.insert(1)
bt.insert(2)
bt.insert(3)
bt.insert(4)
bt.insert(5)
bt.insert(6)
bt.insert(7)

print("Preorder", end=": ") # parent, left, right
bt.traverse_preorder()
print("\nInorder", end=": ") # left, parent, right
bt.traverse_inorder()
print("\nPostorder", end=": ") # left, right, parent
bt.traverse_postorder()  