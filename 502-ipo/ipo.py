class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = list(zip(capital, profits))
        projects.sort(key=lambda x:x[0])
        heap = []
        i, numProjects = 0, 0
        while numProjects < k:
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(heap, -projects[i][1])
                i += 1
            if not heap:
                return w
            profit = -heapq.heappop(heap)
            numProjects += 1
            w += profit
        return w

