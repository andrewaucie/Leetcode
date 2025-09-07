class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currSum = 0
        for n in nums:
            currSum += n
            if currSum < n:
                currSum = n
            maxSum = max(maxSum, currSum)
        return maxSum