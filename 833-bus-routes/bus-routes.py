class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        # Preprocess graph, source -> connected buses -> target
        graph = defaultdict(set)
        for i in range(len(routes)):
            setI = set(routes[i])
            if source in setI:
                graph[-1].add(i)
            if target in setI:
                graph[i].add("target")
            for j in range(i+1, len(routes)):
                setJ = set(routes[j])
                mergedSet = setI.union(setJ)
                if len(mergedSet) < len(routes[i]) + len(routes[j]):
                    graph[i].add(j)
                    graph[j].add(i)

        # Run BFS start from (-1) nodes until reach -2                
        queue = deque()
        for bus in graph[-1]:
            queue.append((bus, 0))

        visited = set()
        while queue:
            bus, num = queue.popleft()
            if bus == "target":
                return num
            for connectedBus in graph[bus]:
                if connectedBus not in visited:
                    visited.add(connectedBus)
                    queue.append((connectedBus, num+1))
        return -1