class HandleError:
  @staticmethod
  def check_value_if_none(value):
    if value is None:
      raise Exception("Value cannot be none or empty")

  @staticmethod
  def check_if_index_in_range(index, start, end):
    if index < start or index > end:
      raise Exception("Index should be in range -1 to total length-1")

class Node:
  def __init__(self, value):
    HandleError.check_value_if_none(value)

    self.value = value
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.length = 0

  def insert(self, value, index = -1):
    HandleError.check_value_if_none(value)
    HandleError.check_if_index_in_range(index, -1, self.length)

    if index == 0:
      self.__insert_at_start(value)
    elif index == -1:
      self.__insert_at_end(value)
    else:
      self.__insert_at_index(value, index)
    self.length += 1

  def search(self, value):
    HandleError.check_value_if_none(value)

    index = 0
    current_node = self.head
    while current_node is not None:
      if current_node.value == value:
        return index
      current_node = current_node.next
      index += 1
    return -1

  def delete(self, index:int =-1):
    HandleError.check_if_index_in_range(index, -1, self.length-1)

    if index == 0:
      self.__delete_at_start()
    elif index == -1:
      self.__delete_at_end()
    else:
      self.__delete_at_index(index)
    self.length -= 1

  def display(self):
    current_node = self.head
    while current_node is not None:
      print(current_node.value, end=" --> ")
      current_node = current_node.next
    print("None")

  def __insert_at_start(self, value):
    if self.head is None:
      self.head = Node(value)
    else:
      current_head = self.head
      self.head = Node(value)
      self.head.next = current_head

  def __insert_at_end(self, value):
    if self.head is None:
      self.__insert_at_start(value)
    else:
      current_node = self.head
      while current_node.next is not None:
        current_node = current_node.next
      current_node.next = Node(value)

  def __insert_at_index(self, value, index):
    current_node = self.head
    for _ in range(1, index):
      current_node = current_node.next
    next_node = current_node.next
    current_node.next = Node(value)
    current_node.next.next = next_node

  def __delete_at_start(self):
    if self.head is not None:
      self.head = self.head.next

  def __delete_at_end(self):
    current_node = self.head
    while current_node.next is not None and current_node.next.next is not None:
      current_node = current_node.next
    current_node.next = None

  def __delete_at_index(self, index):
    current_node = self.head
    for _ in range(1, index):
      current_node = current_node.next
    current_node.next = current_node.next.next
    
# Test
ll = SinglyLinkedList()

ll.insert(5)
ll.display() # 5 --> None
ll.insert(10, 0)
ll.display() # 10 --> 5 --> None
ll.insert(15, 1)
ll.display() # 10 --> 15 --> 5 --> None
ll.insert(20)
ll.display() # 10 --> 15 --> 5 --> 20 --> None

print("Length:", ll.length) # Length: 4
print(ll.search(15)) # 1
print(ll.search(16)) # -1

ll.delete(1)
ll.display() # 10 --> 5 --> 20 --> None
ll.delete(1)
ll.display() # 10 --> 20 --> None
ll.delete()
ll.display() # 10 --> None
ll.delete(0)
ll.display() # None