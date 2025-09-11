class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq = collections.defaultdict(int)
        # for n in nums:
        #     freq[n] += 1
        # heap = []
        # for num, numFreq in freq.items():
        #     if len(heap) == k and heap[0][0] < numFreq:
        #         heapq.heappop(heap)
        #     if len(heap) < k:
        #         heapq.heappush(heap, (numFreq, num))
        # return [num for numFreq, num in heap]
        freq = collections.defaultdict(int)
        buckets = [set() for _ in range(len(nums)+1)]
        for n in nums:
            if n in freq:
                buckets[freq[n]].remove(n)
            freq[n] += 1
            buckets[freq[n]].add(n)
        topK = []
        for i in range(len(buckets)-1, -1, -1):
            for n in buckets[i]:
                topK.append(n)
                if len(topK) == k:
                    return topK
        return topK
            