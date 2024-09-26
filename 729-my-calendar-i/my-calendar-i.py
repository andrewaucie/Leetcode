class MyCalendar:

    def __init__(self):
        self.L = []
        self.m = {}
        
    def book(self, start: int, end: int) -> bool:
        idx = bisect.bisect_right(self.L, start)
        if idx == len(self.L) or self.m[self.L[idx]] >= end:
            bisect.insort(self.L, end)
            self.m[end] = start
            return True

        return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)