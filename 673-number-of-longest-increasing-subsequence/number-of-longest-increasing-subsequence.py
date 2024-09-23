class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [[1,1] for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j][0] + 1 > dp[i][0]:
                        dp[i] = list([dp[j][0] + 1, dp[j][1]])
                    elif dp[j][0] + 1 == dp[i][0]:
                        dp[i][1] += dp[j][1]
        longest = max(dp, key=lambda x:x[0])[0]
        count = 0
        for length, num in dp:
            if longest == length:
                count += num
        return count