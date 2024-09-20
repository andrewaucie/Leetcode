class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        dirxns = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        memo = [[-1] * n for _ in range(m)]
        res = 0
        def dfs(row, col):
            if memo[row][col] != -1:
                return memo[row][col]
            count = 1
            for dx, dy in dirxns:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] > grid[row][col]:
                    count += dfs(new_row, new_col)
            memo[row][col] = count
            return count
        for row in range(m):
            for col in range(n):
                res += dfs(row, col)
        return res % MOD