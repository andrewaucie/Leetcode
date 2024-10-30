class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        heap = [(-grid[0][0], (0,0))]
        visited = set()
        while heap:
            score, (x,y) = heappop(heap)
            if (x,y) == (m-1, n-1):
                return -score
            for dx,dy in (0,1),(1,0),(-1,0),(0,-1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    minScore = max(score, -grid[nx][ny])
                    heappush(heap, (minScore, (nx, ny)))
        return 0