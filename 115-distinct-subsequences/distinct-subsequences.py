class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        memo = [[-1] * (len(t)+1) for _ in range(len(s)+1)]
        def memoization(i,targetIndex):
            if targetIndex == len(t):
                return 1
            if i == len(s):
                return 0
            if memo[i][targetIndex] != -1:
                return memo[i][targetIndex]
            include, exclude = 0, 0
            if s[i] == t[targetIndex]:
                include = memoization(i+1, targetIndex+1)
            exclude = memoization(i+1, targetIndex)
            memo[i][targetIndex] = include + exclude
            return memo[i][targetIndex]

        dp = [0] * (len(t)+1)
        for i in range(len(s)-1, -1, -1):
            nextDP = [0] * (len(t)+1)
            dp[-1] = 1
            for j in range(len(t)-1, -1, -1):
                if s[i] == t[j]:
                    nextDP[j] += dp[j+1]
                nextDP[j] += dp[j]
            dp = nextDP
        return dp[0]