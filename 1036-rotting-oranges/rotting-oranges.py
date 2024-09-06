class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh.add((i,j))
        if len(fresh) == 0:
            return 0
        if len(queue) == 0:
            return -1

        queue.append((-1,-1))
        minutes = 0
        direction = {(0,1), (1,0), (0,-1), (-1,0)}
        while queue:
            i,j = queue.popleft()
            if (i,j) == (-1,-1) and len(queue) != 0:
                queue.append((-1,-1))
                minutes += 1
                continue
            for dx,dy in direction:
                if (i+dx, j+dy) in fresh:
                    fresh.remove((i+dx, j+dy))
                    queue.append((i+dx,j+dy))
        return minutes if len(fresh) == 0 else -1