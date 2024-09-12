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

        # Optimized memoization
        def memoizationOpt(indexSmall, indexLarge):
            if indexSmall == len(text2) or indexLarge == len(text1):
                return 0
            if memo[indexSmall][indexLarge] > 0:
                return memo[indexSmall][indexLarge]
            if text1[indexLarge] == text2[indexSmall]:
                memo[indexSmall][indexLarge] = memoizationOpt(indexSmall+1, indexLarge+1) + 1
            else:
                memo[indexSmall][indexLarge] = max(memoizationOpt(indexSmall+1, indexLarge), memoizationOpt(indexSmall, indexLarge+1))
            return memo[indexSmall][indexLarge]
        # DP Solution
        dp = [[0] * (len(text1)+1) for _ in range(len(text2) + 1)]
        for i in range(len(text2)-1, -1, -1):
            for j in range(len(text1)-1, -1, -1):
                if text2[i] == text1[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        return dp[0][0]
        #return memoizationOpt(0, 0)
            
