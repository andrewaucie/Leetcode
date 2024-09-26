class MyCalendar:

    def __init__(self):
        self.events = []


    def book(self, start: int, end: int) -> bool:
        # [(pos, "start"), (pos, "end"), etc]
        heap = list(self.events)
        heapq.heappush(heap, (start, "start"))
        heapq.heappush(heap, (end, "end"))
        count = 0
        while heap:
            time, eventType = heapq.heappop(heap)
            if eventType == "start":
                count += 1
            else:
                count -= 1
            if count > 1:
                return False
        heappush(self.events, (start, "start"))
        heappush(self.events, (end, "end"))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)