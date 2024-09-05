class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i,j,visited):
            if (i,j) in visited:
                return
            visited.add((i,j))
            if i+1 < len(grid) and grid[i+1][j] == 1:
                dfs(i+1,j,visited)
            if j+1 < len(grid[0]) and grid[i][j+1] == 1:
                dfs(i,j+1,visited)
            if i-1 >= 0 and grid[i-1][j] == 1:
                dfs(i-1,j,visited)
            if j-1 >= 0 and grid[i][j-1] == 1:
                dfs(i,j-1,visited)
        
        maxArea = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    visitedPrev = len(visited)
                    dfs(i,j,visited)
                    visitedAfter = len(visited)
                    print(visited)
                    maxArea = max(maxArea, visitedAfter-visitedPrev)
        return maxArea