class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        d = {(0,1),(1,0),(0,-1),(-1,0)}
        queue = [(grid[0][0], (0,0))]
        heapq.heapify(queue)
        visited = set()
        peak = grid[0][0]
        while queue:
            currPeak, (i,j) = heapq.heappop(queue)
            peak = max(peak, currPeak)
            if (i,j) == (n-1, m-1):
                return peak
            for x,y in d:
                if (0 <= i+x < n and 0 <= j+y < m) and (i,j,x,y) not in visited:
                    visited.add((i,j,x,y))
                    heapq.heappush(queue, (max(grid[i+x][j+y], currPeak), (i+x,j+y)))
        return peak