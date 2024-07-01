class Node:
	def __init__(self, data):
		if data is None:
			raise Exception("Value cannot be none")

		self.data = data
		self.next = None

class SinglyLinkedList:
	def __init__(self):
		self.__head = None
		self.__length = 0
	
	def __len__(self) -> int:
		return self.__length
	
	def __str__(self) -> str:
		self.__traverse(len(self)+1, True)
		return "None"
	
	def insert(self, value, index:int=-1) -> None:
		if index < -1 or index > len(self):
			raise Exception("Index out of bounds")
		
		if index == 0 or not self.__head:
			self.__insert_head(value)
		elif index == -1 or index == len(self):
			self.__insert_tail(value)
		else:
			self.__insert_between(value, index)
		
		self.__length += 1
	
	def delete(self, index:int=-1):
		if index < -1 or index > len(self):
			raise Exception("Index out of bound")
		
		if not self.__head:
			return None
		
		self.__length -= 1

		if index == 0 or not self.__head.next:
			return self.__delete_head()
		if index == -1 or index == len(self)-1:
			return self.__delete_tail()
		return self.__delete_between(index)
	
	def __delete_head(self):
		value = self.__head.data
		self.head = self.__head.next
		return value
	
	def __delete_tail(self):
		tail_node = self.__traverse(len(self))
		value = tail_node.data
		tail_node.next = None
		return value
	
	def __delete_between(self, index):
		node = self.__traverse(index)
		value = node.next.data
		node.next = node.next.next
		return value
	
	def __insert_head(self, value) -> None:
		new_node = Node(value)
		new_node.next = self.__head
		self.__head = new_node
	
	def __insert_tail(self, value) -> None:
		new_node = Node(value)
		tail_node = self.__traverse(len(self))
		tail_node.next = new_node
	
	def __insert_between(self, value, index:int) -> None:
		new_node = Node(value)
		node = self.__traverse(index)
		new_node.next = node.next
		node.next = new_node

	def __traverse(self, index, should_print=False) -> Node:
		counter = 0
		current_node = self.__head
		while counter < index-1:
			if should_print:
				print(current_node.data, end=" > ")
			current_node = current_node.next
			counter += 1
		return current_node

s = SinglyLinkedList()
s.insert(1)
s.insert(2)
s.insert(3)
s.insert(4)
s.insert(5)
print(s)
s.delete()
print(s)