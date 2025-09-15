class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = None
        self.front = None
        self.rear = None
        self.k = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.size += 1
        node = Node(val=value)
        if not self.front:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        # front == rear
        if self.front == self.rear:
            self.front = None
            self.rear = None
            return True
        nextFront = self.front.next
        self.front.next = None
        self.front = nextFront
        return True  

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.rear.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()