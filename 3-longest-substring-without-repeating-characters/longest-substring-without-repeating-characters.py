class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = collections.defaultdict(int)
        left, right = 0, 0
        longestSub = 0
        while right < len(s):
            freq[s[right]] += 1
            while freq[s[right]] > 1:
                freq[s[left]] -= 1
                left += 1
            longestSub = max(longestSub, right - left + 1)
            right += 1
        return longestSub