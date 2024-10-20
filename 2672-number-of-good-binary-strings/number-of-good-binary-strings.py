class Solution:
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        dp = [-1] * (maxLength + 1)
        def dfs(i):
            if i > maxLength:
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = dfs(i + oneGroup) + dfs(i + zeroGroup) + int(i >= minLength)
            dp[i] %= 10**9 + 7
            return dp[i]
        return dfs(0)
