class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        freq = Counter(nums)
        nums = sorted(list(set(nums)))
    
        if len(nums) == 1:
            return nums[0] * freq[nums[0]]
    
        dp = [0] * len(nums)
        dp[0] = nums[0] * freq[nums[0]]
        dp[1] = max(dp[0], nums[1] * freq[nums[1]] + dp[0] * int(nums[1] > nums[0]+1))
        for i in range(2, len(nums)):
            earn = nums[i] * freq[nums[i]]
            dp[i] = max(dp[i-2] + earn, dp[i-1] + earn * int(nums[i] > nums[i-1] + 1))
        return dp[-1]
                        
