class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # DP
        dp = [1] * len(nums)
        res = 1
        for i in range(len(nums)):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    res = max(res, dp[i])
        return res
