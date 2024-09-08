class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        N = len(nums)

        score = 0
        mx = nums[0]

        for i in range(1, N):
            score += mx
            if nums[i] > mx:
                mx = nums[i]
        return score