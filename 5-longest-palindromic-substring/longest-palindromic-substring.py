class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Brute force
        # if len(s) <= 1:
        #     return s
        # maxLen = 1
        # maxStr = s[0]
        # for i in range(len(s)-1):
        #     for j in range(i+1, len(s)):
        #         if j-i+1 > maxLen and s[i: j+1] == s[i: j+1][::-1]:
        #             maxLen = j-i+1
        #             maxStr = s[i:j+1]
        # return maxStr

        # Expand around centers
        def expand(i,j):
            left = i
            right = j +1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        maxStr = s[0]

        for i in range(len(s)-1):
            odd = expand(i,i)
            even = expand(i,i+1)
            if len(odd) > len(maxStr):
                maxStr = odd
            if len(even) > len(maxStr):
                maxStr = even
        return maxStr