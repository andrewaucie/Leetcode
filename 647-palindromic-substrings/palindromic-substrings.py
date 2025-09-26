class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        for center in range(len(s)):
            # odd length palindrome: l [c] r
            left, right = center, center
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                total += 1
            # even length palindrome: l [c] [c] r
            if center < len(s)-1 and s[center] == s[center+1]:
                left = center
                right = center + 1
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    left -= 1
                    right += 1
                    total += 1
        return total