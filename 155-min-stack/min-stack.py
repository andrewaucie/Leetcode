class MinStack:

    def __init__(self):
        self.stack = {} # { 1 : [val, min] , 2 : [val, min] , 3 : [val, min]}
        self.idx = 0        

    def push(self, val: int) -> None:
        self.idx += 1
        self.stack[self.idx] = [val, val]
        if len(self.stack) > 1:
            minValue = min(val, self.stack[self.idx-1][1])
            self.stack[self.idx][1] = minValue

    def pop(self) -> None:
        del self.stack[self.idx]
        self.idx -= 1
        return

    def top(self) -> int:
        return self.stack[self.idx][0]

    def getMin(self) -> int:
        return self.stack[self.idx][1]        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()