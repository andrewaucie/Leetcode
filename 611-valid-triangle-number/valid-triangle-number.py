class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        for a in range(len(nums)):
            for b in range(a+1, len(nums)):
                l, r = b+1, len(nums)-1
                while l < r:
                    m = (l + r + 1) // 2
                    if nums[m] >= nums[a] + nums[b]:
                        r = m - 1
                    else:
                        l = m
                if b < l < len(nums) and nums[l] < nums[a] + nums[b]:
                    total += (l - b)
        return total