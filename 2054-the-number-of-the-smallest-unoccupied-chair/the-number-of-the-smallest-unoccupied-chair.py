class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        available = [i for i in range(len(times))]
        heapq.heapify(available)
        # 1 = start, 0 = end
        events = []
        for i, (arrive, leave) in enumerate(times):
            events.append((arrive, "start", i))
            events.append((leave, "end", i))
        events.sort()

        chairs = [-1] * len(times)
        for time, event, i in events:
            if event == "start":
                chairs[i] = heapq.heappop(available)
            elif event == "end":
                heapq.heappush(available, chairs[i])
                chairs[i] = -1
            if i == targetFriend:
                return chairs[i]
        return chairs[i]