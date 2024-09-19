class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        i = 0
        while i < count[0]:
            nums[i] = 0
            i += 1
        while i < count[0] + count[1]:
            nums[i] = 1
            i += 1
        while i < len(nums):
            nums[i] = 2
            i += 1