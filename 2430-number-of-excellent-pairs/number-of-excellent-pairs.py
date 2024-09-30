class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        pairs = 0
        counter = [0] * 32
        for num in set(nums):
            counter[bin(num).count('1')] += 1
        
        for i in range(32):
            for j in range(32):
                if i + j >= k:
                    pairs += counter[i] * counter[j]
        return pairs
        pairs = 0
