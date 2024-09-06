class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n)]
        rank = [0] * n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            xroot, yroot = find(x), find(y)
            if xroot != yroot:
                if rank[xroot] > rank[yroot]:
                    parent[yroot] = xroot
                else:
                    parent[xroot] = parent[yroot]
                    if rank[xroot] == rank[yroot]:
                        rank[yroot] += 1
        for edge in edges:
            a,b = edge[0] - 1, edge[1] - 1
            if find(a) == find(b):
                return edge
            else:
                union(a,b)
        return []