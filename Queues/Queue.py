class Queue:
    def __init__(self):
        self.__items = []
        self.__front = 0

    def __str__(self) -> str:
        return str(self.__items)
    
    def __len__(self) -> int:
        return len(self.__items)
    
    def enqueue(self, item:int) -> None:
        self.__items.append(item)
    
    def dequeue(self) -> int:
        return self.__items.pop(self.__front) if not self.is_empty() else None
    
    def peek(self) -> int:
        return self.__items[self.__front] if not self.is_empty() else None

    def is_empty(self) -> bool:
        return not len(self)

class UnitTest:
    @staticmethod
    def run_positive_test():
        queue = Queue()

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
        queue = Queue()

        assert queue.dequeue() == None, "Dequeue test failed"
        assert queue.peek() == None, "Peek test failed"

        print("All negative test cases passed")
    
UnitTest.run_positive_test()
UnitTest.run_negative_test()