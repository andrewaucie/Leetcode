class MyCalendar:

    def __init__(self):
        self.l = [(-1, -1), (10**9+1, 10**9+1)]

    def book(self, start: int, end: int) -> bool:
        index = bisect.bisect_left(self.l, (start, end))
        if self.l[index - 1][1] > start or self.l[index][0] < end:
            return False
        self.l.insert(index, (start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)