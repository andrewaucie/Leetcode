class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        left = 0
        right = max(nums) // y + 1
        minSteps = right
        while left < right - 1:
            mid = (right + left) // 2
            if self.canComplete(nums, mid, x, y):
                minSteps = mid
                right = mid
            else:
                left = mid
        return minSteps

    def canComplete(self, nums, steps, x, y):
        diff = x - y
        x_steps = steps
        for i in nums:
            if i > steps * y:
                remain = i - steps * y
                if remain % diff == 0:
                    x_steps -= remain // diff
                else:
                    x_steps -= remain // diff + 1
                if x_steps < 0:
                    return False
        return True