from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)

        # If the absolute target is larger than the total sum, it's impossible to achieve
        if abs(target) > totalSum:
            return 0
        
        # DP table: rows are the indices of the numbers, columns represent possible sums (shifted by totalSum)
        dp = [[0] * (totalSum * 2 + 1) for _ in range(len(nums))]
        
        # Initialize for the first number
        dp[0][totalSum - nums[0]] += 1
        dp[0][totalSum + nums[0]] += 1
        
        # Fill the DP table
        for i in range(1, len(nums)):
            for k in range(-totalSum, totalSum + 1):
                if dp[i - 1][totalSum + k] > 0:
                    dp[i][totalSum + k + nums[i]] += dp[i - 1][totalSum + k]
                    dp[i][totalSum + k - nums[i]] += dp[i - 1][totalSum + k]
        
        # Return the result for achieving target
        return dp[len(nums) - 1][totalSum + target]
