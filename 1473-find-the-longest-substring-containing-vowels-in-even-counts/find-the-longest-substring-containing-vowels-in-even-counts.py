class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        bitmask = {
            "a": 1,
            "e": 2,
            "i": 4,
            "o": 8,
            "u": 16
        }
        mapy = [-2] * 32
        mapy[0] = -1

        max_len = 0
        mask = 0

        for i, char in enumerate(s):
            if char in bitmask:
                mask ^= bitmask[char]

            prev = mapy[mask]
            if prev == -2:
                mapy[mask] = i
            else:
                max_len = max(max_len, i - prev)

        return max_len