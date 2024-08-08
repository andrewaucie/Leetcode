class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        n = len(s)
        for c in range(ord('A'), ord('Z') + 1):
            c = chr(c)
            i, j, replaced = 0, 0, 0
            while j < n:
                if s[j] == c:
                    j += 1
                elif replaced < k:
                    j += 1
                    replaced += 1
                elif s[i] == c:
                    i += 1
                else:
                    i += 1
                    replaced -= 1
                ans = max(ans, j - i)
        return ans