class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxElement = nums[0]
        count = 0
        for n in nums:
            if count == 0:
                maxElement = n
            if maxElement == n:
                count += 1
            else:
                count -= 1
        return maxElement