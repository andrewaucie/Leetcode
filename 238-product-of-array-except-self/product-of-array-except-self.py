class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        # 1 1 2 3 4
        # res[3] = res[2] * 2
        suffixProduct = 1
        for i in range(len(nums)-2, -1, -1):
            suffixProduct *= nums[i+1]
            res[i] *= suffixProduct
        # res[3] *= suffixProduct
        return res
