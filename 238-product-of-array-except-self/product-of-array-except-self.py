class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = [n for n in nums]
        prefixProduct.append(1)
        for i in range(1, len(nums)):
            prefixProduct[i] *= prefixProduct[i-1]

        suffixProduct = [n for n in nums]
        suffixProduct.append(1)
        for i in range(len(nums)-2, -1, -1):
            suffixProduct[i] *= suffixProduct[i+1]
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = prefixProduct[i-1] * suffixProduct[i+1]
        return res
