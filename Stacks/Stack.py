class Stack:
    def __init__(self):
        self.items = []
        self.__last = -1
    
    def __len__(self) -> int:
        return len(self.items)
    
    def __str__(self) -> str:
        return str(self.items)
    
    def push(self, item:int) -> None:
        self.items.append(item)
    
    def pop(self) -> int:
        return self.items.pop() if not self.is_empty() else None
    
    def peek(self) -> int:
        return self.items[self.__last] if not self.is_empty() else None
    
    def is_empty(self) -> bool:
        return not len(self)

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
        assert len(stack) == 1, "Length test case failed"

        stack.push(3)
        assert stack.peek() == 3, "Peek test case failed"
        assert stack.pop() == 3, "Push pop test case failed"
        assert len(stack) == 1, "Length test case failed"

        print("All positive test cases passed")
    
    @staticmethod
    def run_negative_tests():
        stack = Stack()

        assert stack.pop() == None, "Pop test case failed"
        assert stack.peek() == None, "Peek test case failed"

        print("All negative test cases passed")

UnitTest.run_positive_tests()
UnitTest.run_negative_tests()