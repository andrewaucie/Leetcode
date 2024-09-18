class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries = sorted((val, i) for i, val in enumerate(queries))
        res = [-1] * len(queries)
        intervalIndex = 0
        heap = []
        for query, index in queries:
            while intervalIndex < len(intervals) and intervals[intervalIndex][0] <= query:
                heappush(heap, (intervals[intervalIndex][1] - intervals[intervalIndex][0] + 1, intervals[intervalIndex][1]))
                intervalIndex += 1
            while heap and heap[0][1] < query:
                heappop(heap)

            res[index] = heap[0][0] if heap else -1
        return res