class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i, [a, b] in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))
        
        queue = [(-1, start_node)]
        visited = set()
        while queue:
            currProb, currNode = heapq.heappop(queue)
            if currNode == end_node:
                return -currProb
            visited.add(currNode)
            for nextNode, nextProb in graph[currNode]:
                if nextNode not in visited:
                    heapq.heappush(queue, (nextProb*currProb, nextNode))
        return 0