class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        indegree = [0] * n
        for a,b in edges:
            graph[a].append(b)
            indegree[b] += 1
        champion = -1
        for i in range(n):
            if indegree[i] == 0:
                if champion > -1:
                    return -1
                champion = i
        return champion
        
        