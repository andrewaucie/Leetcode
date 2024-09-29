class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for num, start, end in trips:
            # add num when pickup, -num when drop off
            events.append((start, num))
            events.append((end, -num))
        events.sort()
        for i in range(len(events)):
            capacity -= events[i][1]
            if capacity < 0:
                return False
        return True