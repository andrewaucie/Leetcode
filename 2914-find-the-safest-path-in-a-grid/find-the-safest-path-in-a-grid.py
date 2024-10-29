class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # 0 0 0 1
        # 0 0 0 0 
        # 0 0 0 0
        # 1 0 0 0
        # greedy "brute force"
        # look at adjacent cells, compare with thieves, store max distance along path
        n = len(grid)
        # bfs starting with thieves
        minDist = defaultdict(lambda: float('inf'))
        thieves = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    minDist[(i,j)] = 0
                    thieves.append((i,j))
        queue = deque((thief, 0) for thief in thieves)
        while queue:
            (x,y), dist = queue.popleft()
            grid[x][y] = dist
            for dx,dy in (0,1),(1,0),(-1,0),(0,-1):
                if 0 <= x+dx < n and 0 <= y+dy < n and dist + 1 < minDist[(x+dx, y+dy)]:
                    minDist[(x+dx, y+dy)] = dist+1
                    queue.append(((x+dx, y+dy), dist+1))
        
        maxDist = defaultdict(int)
        maxDist[(0,0)] = grid[0][0]
        heap = deque([(0,0)])
        while heap:
            (x,y) = heap.popleft()
            for dx,dy in (0,1),(1,0),(-1,0),(0,-1):
                if 0 <= x+dx < n and 0 <= y+dy < n:
                    newDist = min(maxDist[(x,y)], grid[x+dx][y+dy])
                    if newDist > maxDist[(x+dx, y+dy)]:
                        maxDist[(x+dx, y+dy)] = newDist
                        heap.append((x+dx, y+dy))
        return maxDist[(n-1, n-1)]
        # 3 2 1 0
        # 2 3 2 1 
        # 1 2 2 2
        # 0 1 2 3