class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        freqMax = 0
        for num in nums:
            freq[num] += 1
            freqMax = max(freqMax, freq[num])
        buckets = [[float("-inf")]] * (freqMax+1)
        for f in freq:
            if buckets[freq[f]] == [float("-inf")]:
                buckets[freq[f]] = [f]
            else:
                buckets[freq[f]].append(f)
        res = []
        print(buckets)
        for i in range(freqMax, -1, -1):
            if k == 0:
                break
            if buckets[i] != [float("-inf")]:
                if k - len(buckets[i]) >= 0:
                    res.extend(buckets[i])
                    k -= len(buckets[i])
                else:
                    res.extend(buckets[i][:k])
                    k = 0
        return res