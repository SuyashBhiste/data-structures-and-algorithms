class HandleError:
	@staticmethod
	def check_if_value_is_none(value):
		if value is None:
			raise Exception("value cannot be none")

	@staticmethod
	def check_if_index_is_in_range(index:int, start, end):
		if index < start and index > end:
			raise Exception("Index should be in range -1 to total length-1")

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class CircularLinkedList:
	def __init__(self):
		self.head = None
		self.length = 0

	def insert(self, data, index:int = -1):
		HandleError.check_if_value_is_none(data)
		HandleError.check_if_index_is_in_range(index, -1, self.length-1)

		if index == 0:
			self.__insert_at_start(data)
		elif index == -1 or index == self.length:
			self.__insert_at_end(data)
		else:
			self.__insert_at_index(data, index)
		
		self.length += 1

	def delete(self, index:int = -1):
		HandleError.check_if_index_is_in_range(index, -1, self.length-1)

		if self.head is None:
			return "No nodes in linked list"
		
		if index == 0:
			self.__delete_at_start()
		elif index == -1 or index == self.length-1:
			self.__delete_at_end()
		else:
			self.__delete_at_index(index)
		
		self.length -= 1
	
	def display(self):
		if self.length == 0:
			print("None")
		else:
			current_node = self.head
			while True:
				print(current_node.data, end=" -> ")
				current_node = current_node.next
				if current_node == self.head:
					break
			print(current_node.data)
	
	def find(self, data):
		HandleError.check_if_value_is_none(data)

		index = 0
		is_present = True
		current_node = self.head
		while current_node.data != data:
			current_node = current_node.next
			if current_node == self.head:
				is_present = False
				break
			index += 1
		return index if is_present else -1
	
	def __insert_at_start(self, data):
		if self.head is None:
			self.head = Node(data)
			self.head.next = self.head
		else:
			previous_head = self.head
			self.head = Node(data)
			self.head.next = previous_head

			current_node = previous_head
			while True:
				if current_node.next == previous_head:
					current_node.next = self.head
					break
				current_node = current_node.next
	
	def __insert_at_end(self, data):
		if self.head is None:
			self.__insert_at_start(data)
		else:
			current_node = self.head
			while True:
				if current_node.next == self.head:
					current_node.next = Node(data)
					current_node.next.next = self.head
					break
				current_node = current_node.next
	
	def __insert_at_index(self, data, index: int):
		counter = 0
		current_node = self.head
		while counter < index-1:
			current_node = current_node.next
			index += 1
		next_node = current_node.next
		current_node.next = Node(data)
		current_node.next.next = next_node
	
	def __delete_at_start(self):
		if self.length == 1:
			self.head = None
		else:
			previous_head = self.head
			self.head = previous_head.next

			current_node = previous_head
			while True:
				if current_node.next == previous_head:
					current_node.next = current_node.next.next
					break
				current_node = current_node.next

	def __delete_at_end(self):
		if self.length == 1:
			self.head = None
		else:
			current_node = self.head
			while True:
				if current_node.next.next == self.head:
					current_node.next = current_node.next.next
					break
				current_node = current_node.next
		
	def __delete_at_index(self, index:int):
		counter = 0
		current_node = self.head
		while counter < index-1:
			current_node = current_node.next
			counter += 1
		current_node.next = current_node.next.next

ll = CircularLinkedList()

ll.insert(1)
ll.display()
ll.insert(2, 0)
ll.display()
ll.insert(3, 1)
ll.display()
ll.insert(4, -1)
ll.display()
ll.insert(5, 0)
ll.display()

ll.display()
print(ll.find(4))
print(ll.find(8))

ll.delete()
ll.display()
ll.delete(0)
ll.display()
ll.delete(2)
ll.display()
ll.delete(-1)
ll.display()
ll.delete()
ll.display()