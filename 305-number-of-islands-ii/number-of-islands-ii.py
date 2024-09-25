class UnionFind:
    def __init__(self, n):
        self.parents = [-1] * n  # -1 represents water
        self.rank = [0] * n
        self.count = 0  # Number of islands
    
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
            self.count -= 1  # Merged two islands, so reduce count
    
    def add(self, x):
        if self.parents[x] == -1:  # If it's water, add a new island
            self.parents[x] = x
            self.count += 1

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UnionFind(m * n)
        result = []
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()

        for x, y in positions:
            pos = x * n + y  # Map (x, y) to a 1D index
            
            if (x, y) in visited:
                result.append(uf.count)
                continue
            
            visited.add((x, y))
            uf.add(pos)  # Add new island
            
            # Union with neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) in visited:
                    uf.union(pos, nx * n + ny)
            
            result.append(uf.count)
        
        return result
