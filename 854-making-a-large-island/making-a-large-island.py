class UnionFind:
    def __init__(self, n, m):
        # map (i,j) to linear line
        # (i,j) = n*i + m*j
        # n * m
        # id = (i * m + j)
        self.parents = [m*i + j for i in range(n) for j in range(m)]
        self.islandSize = [1] * (n) * (m)
    
    # find parent of x's connected component
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    # Union
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parents[rootY] = rootX
            self.islandSize[rootX] += self.islandSize[rootY]

class Solution(object):
    def largestIsland(self, grid):
        n, m = len(grid), len(grid[0])
        islandUF = UnionFind(n, m)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    # Check the neighbors and union the land cells
                    for dx, dy in {(-1, 0), (0, -1)}:  # Only check left and top to avoid double union
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                            islandUF.union(i * m + j, ni * m + nj)

        islandMax = max(islandUF.islandSize)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    currIslandSize = 1
                    neighboringRoots = set()  # Track unique neighboring island roots
                    
                    for dx, dy in {(1, 0), (0, 1), (-1, 0), (0, -1)}:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                            parentIsland = islandUF.find(ni * m + nj)
                            if parentIsland not in neighboringRoots:
                                neighboringRoots.add(parentIsland)
                                currIslandSize += islandUF.islandSize[parentIsland]
                    
                    islandMax = max(islandMax, currIslandSize)
        return islandMax