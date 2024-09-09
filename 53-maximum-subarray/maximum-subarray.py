class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMax = float('-inf')
        globalMax = float('-inf')
        for n in nums:
            currMax = max(currMax+n, n)
            globalMax = max(globalMax, currMax)
        return globalMax
        