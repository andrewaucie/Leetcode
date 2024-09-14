class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Align min / max indices
        minNum = min(nums)
        res = 0
        for n in nums:
            if n > minNum:
                res += n - minNum
        return res
        
