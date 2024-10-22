class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()
        prefix = [0]
        for n in nums:
            prefix.append(n + prefix[-1])
        left = 0
        maxLen = 0
        for right in range(1, len(prefix)):
            mid = (left + right) // 2
            val = (prefix[right] - prefix[mid]) - (right - mid) * nums[mid]
            val += (mid - left) * nums[mid] - (prefix[mid] - prefix[left])
            if val > k:
                left += 1
            maxLen = max(maxLen, right - left)
        return maxLen
