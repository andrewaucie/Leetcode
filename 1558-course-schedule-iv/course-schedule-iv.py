class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Build reversed graph in topological sorted order
        # Store indegree (number of ancestors in top sorted order or # of course that this course is a prereq for)
        # Store set of prereq courses for each course
        prereqSet = [set([i]) for i in range(numCourses)]
        indegree = [0] * numCourses
        graph = { i : set() for i in range(numCourses)}
        for prereq, course in prerequisites:
            graph[course].add(prereq)
            indegree[prereq] += 1
        
        # Run BFS on all indegree 0, add to queue if indegree becomes 0 (processed all ancestors and unioned)
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            course = queue.popleft()
            
            # Check ancestors, decrease indegree, merge sets
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                prereqSet[neighbor] = prereqSet[neighbor].union(prereqSet[course])
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        res = []
        # Check if queries are in corresponding prereq set
        for prereq, course in queries:
            res.append((course in prereqSet[prereq]))
        return res
        
        
