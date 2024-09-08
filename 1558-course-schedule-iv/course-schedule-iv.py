class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Build reversed graph in topological sorted order
        graph = {i : set() for i in range(numCourses)}
        for prereq, course in prerequisites:
            graph[prereq].add(course)
        

        def dfs(curr, target, visited):
            if curr == target:
                return True

            for nextCourse in graph[curr]:
                if nextCourse not in visited:
                    visited.add(nextCourse)
                    if dfs(nextCourse, target, visited):
                        return True
            return False

        res = []
        for fromCourse, toCourse in queries:
            res.append(dfs(fromCourse, toCourse, set()))
        return res
