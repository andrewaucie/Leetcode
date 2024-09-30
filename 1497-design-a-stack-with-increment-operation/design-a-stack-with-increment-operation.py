class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [] # [1, 0] is val=1, increment=0
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append([x,0])

    def pop(self) -> int:
        if not self.stack:
            return -1
        val, increment = self.stack.pop()
        if self.stack:
            self.stack[-1][1] += increment
        return val + increment

    def increment(self, k: int, val: int) -> None:
        if not self.stack:
            return
        incIndex = min(k, len(self.stack)) - 1
        self.stack[incIndex][1] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)