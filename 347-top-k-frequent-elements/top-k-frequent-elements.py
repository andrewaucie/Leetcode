class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.defaultdict(int)
        for n in nums:
            freq[n] += 1
        heap = []
        for num, numFreq in freq.items():
            if len(heap) == k and heap[0][0] < numFreq:
                heapq.heappop(heap)
            if len(heap) < k:
                heapq.heappush(heap, (numFreq, num))
        return [num for numFreq, num in heap]
        # maxNum = max(nums)
        # minNum = min(nums)
        # buckets = [0] * (maxNum - minNum + 1)
        # for n in nums:
        #     buckets[]