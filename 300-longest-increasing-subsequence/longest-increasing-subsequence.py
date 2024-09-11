class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Brute Force
        def bruteforce(i, arr):
            if i == len(nums):
                return len(arr)
            include = bruteforce(index+1, [nums[index]])
            exclude = bruteforce(index+1, arr)
            extend = 0
            if len(arr) > 0 and nums[index] > arr[-1]:
                extend = bruteforce(index+1, arr + [nums[index]])
            return max(include, exclude, extend)
        
        # Brute Force + Memo
        memo = {}
        def bruteforce2(i, prev):
            if i == len(nums):
                return 0
            if (i,prev) in memo:
                return memo[(i,prev)]
            include = 0
            exclude = bruteforce2(i+1, prev)
            if nums[i] > prev:
                include = bruteforce2(i+1, nums[i]) + 1
            memo[(i,prev)] = max(include, exclude)
            return memo[(i,prev)]
        
        # DP
        dp = [1] * len(nums)
        res = 1
        for i in range(len(nums)):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    res = max(res, dp[i])
        return res
        return bruteforce2(0, float('-inf'))