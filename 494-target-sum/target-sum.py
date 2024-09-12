class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def memoization(i, curr):
            if i == len(nums):
                return int(curr == target)
            if (i,curr) not in memo:
                add = memoization(i+1, curr + nums[i])
                subtract = memoization(i+1, curr - nums[i])
                memo[(i,curr)] = add + subtract
            return memo[(i,curr)]
        return memoization(0, 0)
