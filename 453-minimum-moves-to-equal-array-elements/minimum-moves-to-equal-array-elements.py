class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minNum = min(nums)
        res = 0
        for n in nums:
            res += n - minNum
        return res
        
