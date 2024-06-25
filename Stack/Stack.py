class Stack:
    def __init__(self):
        self.array = []
    
    def push(self, value:int):
        self.array.append(value)
    
    def pop(self) -> int:
        return self.array.pop() if len(self.array) else -1
    
    def peek(self) -> int:
        return self.array[-1] if len(self.array) else -1
    
    def is_empty(self) -> bool:
        return len(self.array) == 0
    
    def display(self):
        for value in self.array:
            print(value, end=", ")
        print()

st = Stack()
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