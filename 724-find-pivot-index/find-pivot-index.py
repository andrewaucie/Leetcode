class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum, rightSum = 0, sum(nums)
        
        for i in range(len(nums)):
            rightSum -= nums[i]
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        
        return -1