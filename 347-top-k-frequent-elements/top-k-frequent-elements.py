# Python Solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]

        mp = defaultdict(int)
        for num in nums:
            mp[num] += 1
        
        for num, freq in mp.items():
            buckets[freq].append(num)
        
        topK = []
        for i in range(len(buckets)-1, 0, -1):
            for n in buckets[i]:
                topK.append(n)
                if len(topK) == k:
                    return topK
        return topK