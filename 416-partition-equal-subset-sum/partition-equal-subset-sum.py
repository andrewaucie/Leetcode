class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        target //= 2
        
        # Brute Force
        memo = {}
        def bruteforce(i, curr):
            if curr == target:
                return True
            if i == len(nums):
                return False
            if (i,curr) not in memo:
                memo[(i,curr)] = bruteforce(i+1, curr + nums[i]) or bruteforce(i+1, curr)
            return memo[(i,curr)]

        # DP
        dp = [False] * (target+1)
        dp[0] = True
        for n in nums:
            for j in range(target, n-1, -1):
                dp[j] = dp[j] or dp[j - n]
        return dp[target]

        return bruteforce(0, 0)
    
# [1, 5, 11, 5] -> [1, 5, 5, 11]