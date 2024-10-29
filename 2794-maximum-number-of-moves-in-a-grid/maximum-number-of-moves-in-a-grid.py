class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        cache = defaultdict(int)
        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            moves = 0
            for dx in {-1, 0, 1}:
                if 0 <= i+dx < len(grid) and 0 <= j+1 < len(grid[0]):
                    if grid[i+dx][j+1] > grid[i][j]:
                        moves = max(moves, dfs(i+dx, j+1) + 1)
            cache[(i,j)] = moves
            return moves
        
        maxMoves = 0
        for i in range(len(grid)):
            maxMoves = max(maxMoves, dfs(i,0))
        return maxMoves