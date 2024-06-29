class Queue:
    def __init__(self):
        self.array = []

    def __str__(self) -> str:
        return str(self.array)
    
    def __len__(self) -> int:
        return len(self.array)
    
    def push(self, value:int):
        self.array.append(value)
    
    def pop(self):
        if self.is_empty():
            return None
        
        data = self.array[0]
        self.array = self.array[1:]
        return data
    
    def peek(self) -> int:
        return self.array[0] if not self.is_empty() else None

    def is_empty(self) -> bool:
        return not self.array
    
    def clear(self) -> None:
        self.array = []

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