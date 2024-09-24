class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        def isPeak(i):
            if i == 0:
                return nums[i] > nums[i+1]
            elif i == len(nums)-1:
                return nums[i] > nums[i-1]
            else:
                return nums[i] > nums[i+1] and nums[i] > nums[i-1]
        # log(n) = Binary Search
        l = 0
        r = len(nums)-1
        while l < r:
            mid = (l+r) // 2
            if isPeak(mid):
                return mid
            if nums[mid] < nums[mid+1]:
                l = mid+1
            elif nums[mid] < nums[mid-1]:
                r = mid
        return l