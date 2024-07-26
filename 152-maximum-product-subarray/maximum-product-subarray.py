class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        res = cur_max

        for i in range(1, len(nums)):
            num = nums[i]
            temp_max = max(num, cur_max*num, cur_min*num)
            cur_min = min(num, cur_max*num, cur_min*num)
            cur_max = temp_max

            res = max(cur_max, res)
        return res