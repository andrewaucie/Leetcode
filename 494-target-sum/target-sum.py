from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        
        # If the target is out of bounds, no solution exists
        if abs(target) > total:
            return 0
        
        # DP table: rows represent indices of the numbers, columns represent possible sums (shifted by total)
        dp = [[0] * (2 * total + 1) for _ in range(len(nums))]

        # Initialize for the first number (account for both + and - nums[0])
        dp[0][nums[0] + total] = 1
        dp[0][-nums[0] + total] += 1
        
        # Fill the DP table
        for i in range(1, len(nums)):
            for sum_val in range(-total, total + 1):
                if dp[i - 1][sum_val + total] > 0:
                    dp[i][sum_val + nums[i] + total] += dp[i - 1][sum_val + total]
                    dp[i][sum_val - nums[i] + total] += dp[i - 1][sum_val + total]

        # Return the result from the last row
        return dp[len(nums) - 1][target + total]
