class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sort intervals
        # heap to track current ongoing meetings (based on end time)
        # if start >= heap[0] (soonest meeting to finish):
        #      pop heap
        # add current meeting
        # [4] -> check if 5 >= 4 (True)
        # pop heap -> [] -> add 5 as this is now ongoing -> [5]

        # [0,30], [5,10], [30,40], [40,50], [41, 51]
        # [30] -> [10, 30] -> [30, 40] -> [40, 50] -> [41, 50]
        # ---------
        #  -- --
        #   --
        intervals.sort()
        heap = []
        maxMeetings = 0
        for start, end in intervals:
            while heap and start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
            maxMeetings = max(maxMeetings, len(heap))
        return maxMeetings