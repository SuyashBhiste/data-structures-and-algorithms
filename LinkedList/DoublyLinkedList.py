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
  def __init__(self, value):
    HandleError.check_if_value_is_none(value)

    self.data = value
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self):
    self.head  = None
    self.length = 0
  
  def insert(self, value, index:int = -1):
    HandleError.check_if_value_is_none(value)
    HandleError.check_if_index_is_in_range(index, -1, self.length-1)

    if index == 0:
      self.__insert_at_start(value)
    elif index == -1:
      self.__insert_at_end(value)
    else:
      self.__insert_at_index(value, index)
    self.length += 1
  
  def delete(self, index:int = -1):
    HandleError.check_if_index_is_in_range(index, -1, self.length-1)
    
    if index == 0:
      self.__delete_at_start()
    elif index == -1:
      self.__delete_at_end()
    else:
      self.__delete_at_index(index)
    self.length -= 1
  
  def search(self, value):
    index = 0
    current_node = self.head
    while current_node is not None:
      if current_node.data == value:
        return index
      current_node = current_node.next
      index += 1
    return -1

  def display(self):
    current_node = self.head
    while current_node is not None:
      print(current_node.data, end=" <--> ")
      current_node = current_node.next
    print("None")
  
  def __insert_at_start(self, value):
    if self.head is None:
      self.head = Node(value)
    else:
      current_head = self.head
      self.head = Node(value)
      self.head.next = current_head
      current_head.prev = self.head
  
  def __insert_at_end(self, value):
    if self.head is None:
      self.head = Node(value)
    else:
      last_node = self.__iterate_to_index(self.length-1)
      last_node.next  = Node(value)
      last_node.next.prev = last_node
  
  def __insert_at_index(self, value, index):
    previous_node = self.__iterate_to_index(index-1)
    next_node = previous_node.next
    previous_node.next = Node(value)
    previous_node.next.next = next_node
    previous_node.next.prev = previous_node
    next_node.prev = previous_node.next

  def __delete_at_start(self):
    if self.head is not None:
      self.head = self.head.next
      if self.head is not None:
        self.head.prev = None

  def __delete_at_end(self):
    if self.head is not None:
      if self.head.next is None:
        self.__delete_at_start()
      else:
        second_last_node = self.__iterate_to_index(self.length-2)
        second_last_node.next = None

  def __delete_at_index(self, index):
    if index == self.length -1:
      self.__delete_at_end()
    else:
      second_last_node = self.__iterate_to_index(index-1)
      next_node = second_last_node.next.next
      second_last_node.next = next_node
      next_node.prev = second_last_node
  
  def __iterate_to_index(self, index) -> Node:
    current_node = self.head
    for _ in range(1, index+1):
      current_node = current_node.next
    return current_node

ll = DoublyLinkedList()

ll.insert(5)
ll.display() # 5 <--> None
ll.insert(10, 0)
ll.display() # 10 <--> 5 <--> None
ll.insert(15, 1)
ll.display() # 10 <--> 15 <--> 5 <--> None
ll.insert(20)
ll.display() # 10 <--> 15 <--> 5 <--> 20 <--> None

print("Length:", ll.length) # Length: 4
print(ll.search(15)) # 1
print(ll.search(16)) # -1

ll.delete(1)
ll.display() # 10 <--> 5 <--> 20 <--> None
ll.delete(1)
ll.display() # 10 <--> 20 <--> None
ll.delete()
ll.display() # 10 <--> None
ll.delete(0)
ll.display() # None