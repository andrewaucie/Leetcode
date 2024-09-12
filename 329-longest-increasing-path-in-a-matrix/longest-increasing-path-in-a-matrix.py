class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = [[-1] * len(matrix[0]) for _ in range(len(matrix))]
        def memoization(i,j):
            if memo[i][j] != -1:
                return memo[i][j]
            d = {(0,1),(1,0),(0,-1),(-1,0)}

            # Path at (i,j) or No path (i,j)
            res = 1
            for x,y in d:
                if 0 <= i+x < len(matrix) and 0 <= j+y < len(matrix[0]) and matrix[i+x][j+y] > matrix[i][j]:
                    res = max(res, memoization(i+x, j+y) + 1)
            memo[i][j] = res
            return res
         
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, memoization(i,j))
        return res