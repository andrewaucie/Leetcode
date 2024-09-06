class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = set()
        for i in range(n):
            nodes.add(i)
        graph = {i: set() for i in range(n)}
        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)
        queue = deque([0])
        res = 0
        while len(nodes) > 0:
            res += 1
            queue = deque([nodes.pop()])
            while queue:
                curr = queue.popleft()
                for neighbor in graph[curr]:
                    if neighbor in nodes:
                        queue.append(neighbor)
                        nodes.remove(neighbor)
        return res
        