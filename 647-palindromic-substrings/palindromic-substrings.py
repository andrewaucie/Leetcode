class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        if n <= 0:
            return 0

        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
            ans += 1

        for i in range(n - 1):
            dp[i][i + 1] = (s[i] == s[i + 1])
            ans += dp[i][i + 1]

        for length in range(3, n + 1):
            i = 0
            # Checking every possible substring of any specific length
            for j in range(length - 1, len(s)):
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
                ans += dp[i][j]
                i += 1

        return ans

