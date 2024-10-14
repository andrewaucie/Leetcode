class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-n for n in nums]
        heapq.heapify(heap)
        score = 0
        for _ in range(k):
            maxNum = -heapq.heappop(heap)
            score += maxNum
            heapq.heappush(heap, -math.ceil(maxNum / 3))
        return score