class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class Queuell:
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

    def pop(self) -> int:
        if self.head is None:
            return -1
        else:
            data = self.head.data
            self.head = self.head.next
            self.length -= 1
            return data
    
    def peek(self):
        return self.head.data if self.head else -1
    
    def is_empty(self):
        return self.head is None
    
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

ql = Queuell()
print("is_empty", ql.is_empty())

print("Push")
ql.push(1)
ql.display()
print("Push")
ql.push(2)
ql.display()
print("Push")
ql.push(3)
ql.display()

print("Peek", ql.peek())
print("is_empty", ql.is_empty())

print("Pop")
ql.pop()
ql.display()
print("Pop")
ql.pop()
ql.display()
print("Pop")
ql.pop()
ql.display()
