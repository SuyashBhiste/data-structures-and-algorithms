class Stack:
    def __init__(self):
        self.items = []
        self.length = 0
    
    def push(self, item:int) -> None:
        self.items.append(item)
        self.length += 1
    
    def pop(self) -> int:
        if len(self.items):
            self.length -= 1
            return self.items.pop()
    
    def peek(self) -> int:
        return self.items[-1] if len(self.items) else None
    
    def is_empty(self) -> bool:
        return not len(self.items)
    
    def display(self) -> None:
        print(self.items)

class UnitTest:
    @staticmethod
    def run_positive_tests():
        stack = Stack()

        assert stack.is_empty(), "Empty stack test case failed"
        stack.push(1)
        assert not stack.is_empty(), "Empty stack test case failed"

        stack.push(2)
        assert stack.peek() == 2, "Peek test case failed"
        assert stack.pop() == 2, "Push pop test case failed"
        assert stack.length == 1, "Length test case failed"

        stack.push(3)
        assert stack.peek() == 3, "Peek test case failed"
        assert stack.pop() == 3, "Push pop test case failed"
        assert stack.length == 1, "Length test case failed"

        print("All positive test cases passed")
    
    @staticmethod
    def run_negative_tests():
        stack = Stack()

        assert stack.pop() == None, "Pop test case failed"
        assert stack.peek() == None, "Peek test case failed"

        print("All negative test cases passed")

UnitTest.run_positive_tests()
UnitTest.run_negative_tests()