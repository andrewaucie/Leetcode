class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCount = Counter(nums)
        freqList = sorted(freqCount.items(), key=lambda x:x[1], reverse=True)
        freqList = [x[0] for x in freqList]
        print(freqList)
        return freqList[:k]