class Solution:
    def numDecodings(self, s: str) -> int:
        # backtracking
        dp = [-1] * len(s)
        def backtrack(i):
            if i == len(s):
                return 1
            if dp[i] != -1:
                return dp[i]
            if s[i] == '0':
                return 0
            currWays = backtrack(i+1)
            if i < len(s)-1 and (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6')):
                currWays += backtrack(i+2)
            dp[i] = currWays
            return dp[i]
        return backtrack(0)
