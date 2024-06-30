class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None

class Queuell:
    def __init__(self):
        self.__front = None
        self.__rear = None
        self.__length = 0

    def __len__(self) -> int:
        return self.__length
    
    def __str__(self) -> str:
        current_node = self.__front
        while current_node:
            print(current_node.data, end=" > ")
            current_node = current_node.next
        return "None"

    def enqueue(self, value: int):
        new_node = Node(value)
        if self.is_empty():
            self.__front = new_node
            self.__rear = new_node
        else:
            self.__rear.next = new_node
            self.__rear = self.__rear.next
        self.__length += 1

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.__front.data
        self.__front = self.__front.next
        if self.__front is None:
            self.__rear = None
        self.__length -= 1
        return data
    
    def peek(self) -> int:
        return self.__front.data if not self.is_empty() else None
    
    def is_empty(self) -> bool:
        return not self.__front

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