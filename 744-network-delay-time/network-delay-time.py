class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra's Algorithm
        # Run BFS until no nodes left
        # If you see a node with an edge already defined, lower its weight
        # Return minimum weighted length of longest path
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v,w))

        weights = [float('inf')] * (n+1)
        weights[k] = 0

        queue = [(0,k)]
        heapq.heapify(queue)
        visited = set()
        while queue:
            (path, curr) = heapq.heappop(queue)
            for node, weight in graph[curr]:
                if (curr, node) in visited:
                    continue
                visited.add((curr, node))
                if path + weight < weights[node]:
                    weights[node] = path + weight
                    heapq.heappush(queue, (weights[node], node))
        delayTime = max(weights[1:])
        return delayTime if delayTime != float('inf') else -1          
