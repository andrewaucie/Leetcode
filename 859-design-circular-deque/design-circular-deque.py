class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularDeque:

    def __init__(self, k: int):
        self.size = 0
        self.deque = None
        self.back = None
        self.front = None
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if not self.deque:
            self.deque = self.back = self.front = ListNode(val=value)
        else:
            self.front.next = ListNode(prev=self.front, val=value)
            self.front = self.front.next
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if not self.deque:
            self.deque = self.back = self.front = ListNode(val=value)
        else:
            self.back.prev = ListNode(next=self.back, val=value)
            self.back = self.back.prev
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.back:
            self.deque = self.front = self.back = None
        else:
            self.front = self.front.prev
            self.front.next = None
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.back:
            self.deque = self.front = self.back = None
        else:
            self.back = self.back.next
            self.back.prev = None
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.back.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()