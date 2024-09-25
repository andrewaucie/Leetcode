class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [1] * n
        self.islands = 0
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parents[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parents[rootX] = rootY
            else:
                self.parents[rootY] = rootX
                self.rank[rootX] += 1
            self.islands -= 1

    def addIsland(self):
        self.islands += 1
    
    def getIslands(self):
        return self.islands

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UnionFind(len(positions))
        direction = {(1,0),(0,1),(-1,0),(0,-1)}
        visited = {}
        islands = []
        for i, (x, y) in enumerate(positions):
            if (x,y) in visited:
                islands.append(uf.getIslands())
                continue
            uf.addIsland()
            for dx,dy in direction:
                if (x+dx, y+dy) in visited:
                    uf.union(i, visited[(x+dx, y+dy)])
            visited[(x,y)] = i
            islands.append(uf.getIslands())
        return islands
        
