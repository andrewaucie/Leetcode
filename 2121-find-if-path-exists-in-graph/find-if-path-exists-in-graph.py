from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # bfs
        queue = deque()
        queue.append(source)
        visited = set()
        while queue:
            curr = queue.popleft()
            visited.add(curr)
            if curr == destination:
                return True
            for nextEdge in graph[curr]:
                if nextEdge not in visited:
                    queue.append(nextEdge)
        return False

        # dfs