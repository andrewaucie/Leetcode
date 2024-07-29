class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        while maxHeap:
            if len(maxHeap) == 1:
                return -maxHeap[0]
            first = -heapq.heappop(maxHeap)
            second = -heapq.heappop(maxHeap)
            if first > second:
                heapq.heappush(maxHeap, -(first-second))
        return 0
