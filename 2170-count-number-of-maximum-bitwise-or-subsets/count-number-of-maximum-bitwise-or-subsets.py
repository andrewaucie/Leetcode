class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        maxSum = 0
        for num in nums:
            maxSum |= num
        
        dp = {}
        def memoization(i, currSum):
            if i == len(nums):
                return int(currSum == maxSum)
            if (i, currSum) in dp:
                return dp[(i, currSum)]
            take = memoization(i+1, currSum | nums[i])
            skip = memoization(i+1, currSum)
            dp[(i, currSum)] = take + skip
            return dp[(i, currSum)]
            
        return memoization(0, 0)