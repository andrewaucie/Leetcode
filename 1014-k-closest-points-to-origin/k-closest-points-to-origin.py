class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [(-(x**2 + y**2), (x,y)) for x,y in points]
        heapq.heapify(minHeap)
        while len(minHeap) > k:
            heapq.heappop(minHeap)
        return [p[1] for p in minHeap]
