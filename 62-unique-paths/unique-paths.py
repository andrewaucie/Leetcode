class Solution:
    def uniquePaths(self, m: int, n: int) -> int:\
        # Only need row above, and start from left endpoint (=1)
        # Initialize row to 1, since initial row is only one possible path
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j-1]
        return dp[n-1]