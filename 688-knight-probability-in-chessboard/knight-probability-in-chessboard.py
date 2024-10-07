class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # recurse on moves, multiply by number of moves in bound / 8
        knightMoves = {(1,2),(2,1),(-1,2),(1,-2),(-1,-2),(2,-1),(-2,1),(-2,-1)}
        memo = {}
        def move(k, r, c):
            if k == 0:
                return 1
            if (k,r,c) in memo:
                return memo[(k,r,c)]
            paths = 0
            for dx,dy in knightMoves:
                if 0 <= r+dx < n and 0 <= c+dy < n:
                    paths += move(k-1, r+dx, c+dy)
            memo[(k,r,c)] = paths
            return paths
        
        return move(k, row, column) / 8**k