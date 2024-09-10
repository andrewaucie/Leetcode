class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * (len(nums))
        def recurse(nums, i):
            if i < 0:
                return 0
            if memo[i] >= 0:
                return memo[i]
            res = max(recurse(nums, i-2) + nums[i], recurse(nums, i-1))
            memo[i] = res
            return res
        return recurse(nums, len(nums)-1)