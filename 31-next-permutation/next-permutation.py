class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        index, swapIndex = -1, -1
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                index = i-1
                break
        if index == -1:
            self.reverseArray(nums)
            return
        for i in range(index+1, len(nums)):
            if nums[index] >= nums[i]:
                swapIndex = i-1
                break
        nums[index], nums[swapIndex] = nums[swapIndex], nums[index]
        self.reverseArray(nums, index+1)
    
    def reverseArray(self, arr, start=0):
        l, r = start, len(arr)-1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

# [1, 2, 3]
# 1 2 3
# 