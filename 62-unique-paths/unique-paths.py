class Solution:
    def uniquePaths(self, m: int, n: int) -> int:\
        # Only need row above, and start from left endpoint (=1)
        # Initialize row to 1, since initial row is only one possible path
        # DP
        # dp = [1] * n
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[j] = dp[j] + dp[j-1]
        # return dp[n-1]

        # Brute Force
        memo = [[0] * n for _ in range(m)]
        def bruteforce(i, j):
            if i == 0 or j == 0:
                return 1
            if memo[i][j] == 0:
                memo[i][j] = bruteforce(i-1, j) + bruteforce(i, j-1)
            return memo[i][j]

        return bruteforce(m-1, n-1)