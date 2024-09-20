class Solution:
    def shortestPalindrome(self, s: str) -> str:
        begin = ''
        i = -1
        while (begin + s) != (begin + s)[::-1]:
            begin += s[i]
            i -= 1
        return begin + s