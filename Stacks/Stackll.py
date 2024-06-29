class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stackll:
    def __init__(self):
        self.top = None
        self.__length = 0
    
    def __len__(self) -> int:
        return self.__length
    
    def __str__(self):
        current_node = self.top
        while current_node:
            print(current_node.data, end=" > ")
            current_node = current_node.next
        return "None"
    
    def push(self, data) -> None:
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.__length += 1
    
    def pop(self):
        if self.is_empty():
            return None
        
        prev_top = self.top
        self.top = self.top.next
        self.__length -= 1
        return prev_top.data
    
    def peek(self) -> int:
        return self.top.data if not self.is_empty() else None
    
    def is_empty(self) -> bool:
        return not self.top


class UnitTest:
    @staticmethod
    def run_positive_tests():
        stack = Stackll()

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
        stack = Stackll()

        assert stack.pop() == None, "Pop test case failed"
        assert stack.peek() == None, "Peek test case failed"

        print("All negative test cases passed")

UnitTest.run_positive_tests()
UnitTest.run_negative_tests()