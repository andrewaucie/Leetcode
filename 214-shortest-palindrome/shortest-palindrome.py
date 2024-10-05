class Solution:
    def shortestPalindrome(self, s: str) -> str:
        reversedString = s[::-1]
        string = s + "#" + reversedString
        lps = self.LPS(string)[-1]
        prepend = reversedString[: len(s) - lps]
        return prepend + s
    
    def LPS(self, s):
        length = 0
        table = [0] * len(s)
        for i in range(1, len(s)):
            if length > 0 and s[i] != s[length]:
                length = table[length - 1]
            if s[i] == s[length]:
                length += 1
            table[i] = length
        return table
