class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)
        if target > totalSum:
            return 0
        
        dp = [[0] * (totalSum*2 + 1) for _ in range(len(nums))]
        dp[0][totalSum - nums[0]] += 1
        dp[0][totalSum + nums[0]] += 1
        for i in range(1, len(nums)):
            for k in range(-totalSum, totalSum+1):
                if dp[i-1][totalSum + k] > 0:
                    dp[i][totalSum + k + nums[i]] += dp[i-1][totalSum + k]
                    dp[i][totalSum + k - nums[i]] += dp[i-1][totalSum + k]
        return dp[len(nums)-1][totalSum + target]
