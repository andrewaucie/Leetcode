class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)
        if target > totalSum:
            return 0
        
        dp = defaultdict(int)
        dp[totalSum + nums[0]] += 1
        dp[totalSum - nums[0]] += 1
        for i in range(1, len(nums)):
            nextDP = defaultdict(int)
            for prevSum in dp:
                nextDP[prevSum + nums[i]] += dp[prevSum]
                nextDP[prevSum - nums [i]] += dp[prevSum]
            dp = nextDP
        return dp[totalSum + target]
        #     for k in range(-totalSum, totalSum+1):
        #         if dp[totalSum + k] > 0:
        #             nextDP[totalSum + k + nums[i]] += dp[totalSum + k]
        #             nextDP[totalSum + k - nums[i]] += dp[totalSum + k]
        #     dp = nextDP
        # return dp[totalSum + target]
