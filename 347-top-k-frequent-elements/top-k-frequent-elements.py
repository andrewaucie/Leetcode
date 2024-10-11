# Python Solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = [] # [(freq, num)]
        freq = Counter(nums)
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        topK = []
        while heap:
            topK.append(heapq.heappop(heap)[1])
        return topK