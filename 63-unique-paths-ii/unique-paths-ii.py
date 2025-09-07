class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1]*n for _ in range(m)]
        def bruteforce(i,j):
            if not (0 <= i < m) or not (0 <= j < n):
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if i == m-1 and j == n-1:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            ways = bruteforce(i+1, j) + bruteforce(i, j+1)
            dp[i][j] = ways
            return ways
        return bruteforce(0,0)
            