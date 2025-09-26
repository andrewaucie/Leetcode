class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxPr = nums[0]
        minPr = nums[0]
        res = maxPr
        for i in range(1, len(nums)):
            temp = max(nums[i], max(maxPr * nums[i], minPr * nums[i]))
            minPr = min(nums[i], min(maxPr * nums[i], minPr * nums[i]))
            maxPr = temp
            res = max(res, maxPr)
        return res