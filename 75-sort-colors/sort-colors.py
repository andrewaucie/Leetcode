class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last0, first2 = 0, len(nums) - 1
        i = 0
        while i <= first2:
            while i >= last0 and i <= first2 and (nums[i] == 0 or nums[i] == 2):
                if nums[i] == 0:
                    nums[last0], nums[i] = nums[i], nums[last0]
                    last0 += 1
                elif nums[i] == 2:
                    nums[first2], nums[i] = nums[i], nums[first2]
                    first2 -= 1
            i += 1
