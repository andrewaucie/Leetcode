class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        memo = [[-1] * len(grid[0]) for _ in range(len(grid))]
        def backtrack(i,j):
            if memo[i][j] != -1:
                return memo[i][j]
            res = 1
            for dx, dy in {(0,1),(1,0),(0,-1),(-1,0)}:
                if 0 <= i+dx < len(grid) and 0 <= j+dy < len(grid[0]) and grid[i+dx][j+dy] > grid[i][j]:
                   res += backtrack(i+dx, j+dy)
            memo[i][j] = res
            return res
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += backtrack(i,j)
        return res % (10**9 + 7)
