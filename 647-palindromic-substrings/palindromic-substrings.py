class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self.expandAroundCenter(s, i, i) # Odd Length palindrome
            count += self.expandAroundCenter(s, i-1, i) # Even Length palindrome
        return count
    
    def expandAroundCenter(self, s: str, l: int, r: int) -> int:
        ps_count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            ps_count += 1
            l -= 1
            r += 1
        return ps_count       