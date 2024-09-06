class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqs = [0] * numCourses
        adjList = [[] for _ in range(numCourses)]
        ans = 0
        for pair in prerequisites:
            adjList[pair[1]].append(pair[0])
            reqs[pair[0]] += 1
        
        queue = deque()
        for i in range(numCourses):
            if reqs[i] == 0:
                queue.append(i)
        
        while queue:
            current = queue.popleft()
            ans += 1

            for next_course in adjList[current]:
                reqs[next_course] -= 1
                if reqs[next_course] == 0:
                    queue.append(next_course)
        return ans == numCourses
        