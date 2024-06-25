class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class Stackll:
    def __init__(self):
        self.head = None
        self.last = None
        self.length = 0
    
    def push(self, value: int):
        if self.head is None:
            self.head = Node(value)
            self.last = self.head
        else:
            self.last.next = Node(value)
            self.last = self.last.next
        self.length += 1
    
    def pop(self):
        if self.head is None:
            return -1
        elif self.length == 1:
            last_node = self.head
            self.head = None
            self.length -= 1
            return last_node.data
        elif self.length == 2:
            last_node = self.head.next
            self.head.next = None
            self.length -= 1
            return last_node.data
        else:
            current_node = self.head
            while current_node.next.next:
                current_node = current_node.next
            last_node = current_node.next
            current_node.next = current_node.next.next
            self.length -= 1
            return last_node.data
    
    def peek(self):
        return self.last.data if self.head else -1
    
    def is_empty(self):
        return self.head is None
    
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

st = Stackll()
print("is_empty", st.is_empty())
st.push(1)
print("Push")
st.display()
st.push(2)
print("Push")
st.display()
st.push(3)
print("Push")
st.display()

print()
print("Peek", st.peek())
st.display()
print("is_empty", st.is_empty())
print()

print("Pop", end=" ")
print(st.pop())
st.display()
print("Pop", end=" ")
print(st.pop())
st.display()
print("Pop", end=" ")
print(st.pop())
st.display()
