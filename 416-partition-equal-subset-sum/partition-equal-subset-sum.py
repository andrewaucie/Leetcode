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

        # 1D DP
        # dp = [False] * (target+1)
        # dp[0] = True
        # for n in nums:
        #     for j in range(target, n-1, -1):
        #         dp[j] = dp[j] or dp[j - n]

        # return dp[target]

        # 2D DP
        dp = [[False] * (target+1) for _ in range(len(nums)+1)]
        dp[0][0] = True
        for i in range(1, len(nums)+1):
            curr = nums[i-1]
            for j in range(target+1):
                if curr > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-curr]
        return dp[len(nums)][target]
        return bruteforce(0, 0)
    
# [1, 5, 11, 5] -> [1, 5, 5, 11]