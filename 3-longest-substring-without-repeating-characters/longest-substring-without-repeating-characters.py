class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSub = ""
        maxSub = 0
        for i in s:
            if i not in longestSub:
                longestSub += i
            else:
                maxSub = max(maxSub, len(longestSub))
                index = longestSub.index(i)
                longestSub = longestSub[index+1:] + i
        return max(maxSub, len(longestSub))

# if s[i] != s[i-1] and s[i] not in 