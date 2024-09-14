class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0
        curr = 0
        maxNum = max(nums)
        for n in nums:
            if n == maxNum:
                curr += 1
                longest = max(longest, curr)
            else:
                curr = 0
        return longest