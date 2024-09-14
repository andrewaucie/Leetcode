class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0
        curr = 0
        currMax = nums[0]
        for n in nums:
            if n == currMax:
                curr += 1
                longest = max(longest, curr)
            elif n > currMax:
                currMax = n
                curr = 1
                longest = 1
            else:
                curr = 0
        return longest