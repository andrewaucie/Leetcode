class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.friends = [set([i]) for i in range(n)]
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parents[rootY] = rootX
            self.friends[rootX] |= self.friends[rootY]

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # get number of users
        # iterate through logs, union (a,b)
        # if size(parent(a)) == len(users): return timestamp
        # return -1
        logs.sort()
        
        uf = UnionFind(n)
        for timestamp, a, b in logs:
            uf.union(a, b)
            if len(uf.friends[uf.find(a)]) == n:
                return timestamp
        return -1