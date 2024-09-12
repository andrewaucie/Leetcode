class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Brute Force (check every ordering of the smaller text)
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        # Text1 is larger, Text2 is smaller
        # Check largest subsequence of small exists in larger text
        memo = [[0] * len(text1) for _ in range(len(text2))]
        def memoization(indexSmall, indexLarge):
            if indexSmall == len(text2) or indexLarge == len(text1):
                return 0
            if memo[indexSmall][indexLarge] > 0:
                return memo[indexSmall][indexLarge]
            matched = 0
            for i in range(indexLarge, len(text1)):
                if text1[i] == text2[indexSmall]:
                    matched = memoization(indexSmall+1, i+1) + 1
                    break
            unmatched = memoization(indexSmall+1, indexLarge)
            memo[indexSmall][indexLarge] = max(matched, unmatched)
            return memo[indexSmall][indexLarge]
        return memoization(0, 0)
            
