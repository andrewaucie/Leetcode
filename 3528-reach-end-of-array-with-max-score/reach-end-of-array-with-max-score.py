class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        score = 0
        mx = 0
        for n in nums:
            score += mx
            mx = max(mx, n)
        return score