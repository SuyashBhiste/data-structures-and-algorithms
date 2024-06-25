class Queue:
    def __init__(self):
        self.array = []
    
    def push(self, value:int):
        self.array.append(value)
    
    def pop(self) -> int:
        if len(self.array) == 0:
            return -1
        data = self.array[0]
        self.array = self.array[1:]
        return data
    
    def peek(self):
        return self.array[0] if len(self.array) else -1

    def is_empty(self):
        return len(self.array) == 0
    
    def clear(self):
        self.array = []
    
    def display(self):
        for value in self.array:
            print(value, end=" ")
        print()

que = Queue()

print("is_empty", que.is_empty())
print("Push")
que.push(1)
que.display()
print("Clear")
que.clear()
que.display()

print("Push")
que.push(1)
que.display()
print("Push")
que.push(2)
que.display()
print("Push")
que.push(3)
que.display()

print("Peek", que.peek())
print("is_empty", que.is_empty())

print("Pop")
que.pop()
que.display()
print("Pop")
que.pop()
que.display()
print("Pop")
que.pop()
que.display()