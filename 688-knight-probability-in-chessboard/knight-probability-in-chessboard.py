class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # recurse on moves, multiply by number of moves in bound / 8
        knightMoves = {(1,2),(2,1),(-1,2),(1,-2),(-1,-2),(2,-1),(-2,1),(-2,-1)}

        dp = [[[0]*n for _ in range(n)] for _ in range(k+1)]
        dp[0][row][column] = 1

        for move in range(1, k+1):
            for i in range(n):
                for j in range(n):
                    for dx,dy in knightMoves:
                        if 0 <= i+dx < n and 0 <= j+dy < n:
                            dp[move][i][j] += dp[move-1][i+dx][j+dy]
        
        totalMoves = sum(dp[k][i][j] for i in range(n) for j in range(n))
        return totalMoves / 8**k