class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        left, right = 0, max(nums) // min(x, y) + 1
        while left < right:
            mid = (left + right) // 2
            if self.can_reduce_to_zero(nums, x, y, mid):
                right = mid
            else:
                left = mid + 1
        return left

    def can_reduce_to_zero(self, arr, x, y, k):
        required_ops = 0
        for element in arr:
            if element <= k * y:
                continue
            extra_ops = (element - k * y + x - y - 1) // (x - y)
            required_ops += extra_ops
            if required_ops > k:
                return False
        return True
