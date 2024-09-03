class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        suffix = [0] * len(nums)
        suffixSum = 0
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = suffixSum
            suffixSum += nums[i]

        prefixSum = 0
        for i in range(len(nums)):
            if prefixSum == suffix[i]:
                return i
            prefixSum += nums[i]
        return -1