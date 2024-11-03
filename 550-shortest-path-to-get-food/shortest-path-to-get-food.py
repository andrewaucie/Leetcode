class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '*':
                    queue.append(((i,j), 0))
                    break
            if queue:
                break
        visited = set()
        while queue:
            (x,y), dist = queue.popleft()
            if grid[x][y] == '#':
                return dist
            for dx,dy in {(-1,0),(0,-1),(1,0),(0,1)}:
                nx = dx + x
                ny = dy + y
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != 'X' and (nx,ny) not in visited:
                    visited.add((nx,ny))
                    queue.append(((nx,ny), dist+1))
        return -1