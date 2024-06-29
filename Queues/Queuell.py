class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class Queuell:
    def __init__(self):
        self.front = None
        self.rear = None
        self.__length = 0

    def __len__(self) -> int:
        return self.__length
    
    def __str__(self) -> str:
        current_node = self.front
        while current_node:
            print(current_node.data, end=" > ")
            current_node = current_node.next
        return "None"

    def enqueue(self, value: int):
        new_node = Node(value)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if self.is_empty():
            self.front = self.rear
        self.__length += 1

    def dequeue(self):
        if self.front is None:
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.__length -= 1
        return data
    
    def peek(self) -> int:
        return self.front.data if self.front else None
    
    def is_empty(self) -> bool:
        return not self.front

class UnitTest:
    @staticmethod
    def run_positive_test():
        queue = Queuell()

        assert queue.is_empty(), "Empty queue test failed"
        queue.enqueue(1)
        assert not queue.is_empty(), "Empty queue test failed"

        queue.enqueue(2)
        assert queue.peek() == 1, "Peek test failed"
        assert queue.dequeue() == 1, "Enqueue dequeue test failed"
        assert len(queue) == 1, "Length test failed"

        queue.enqueue(3)
        assert queue.peek() == 2, "Peek test failed"
        assert queue.dequeue() == 2, "Enqueue dequeue test failed"
        assert len(queue) == 1, "Length test failed"

        print("All positive test cases passed")

    @staticmethod
    def run_negative_test():
        queue = Queuell()

        assert queue.dequeue() == None, "Dequeue test failed"
        assert queue.peek() == None, "Peek test failed"

        print("All negative test cases passed")
    
UnitTest.run_positive_test()
UnitTest.run_negative_test()