class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        maxLen = 0
        left, right = 0, 0
        freq = defaultdict(int)
        while right < len(nums):
            freq[nums[right]] += 1
            while freq[nums[right]] > k: 
                freq[nums[left]] -= 1
                left += 1
            maxLen = max(maxLen, right - left + 1)
            right += 1
        return maxLen