class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        abj={}
        for i,j in prerequisites:
            if i not in abj:
                abj[i]=[j]
            else:
                abj[i].append(j)
        def div(start,end):
            vis=[]

            def dfs(node):
                if node==end:
                    return True
                if node not in abj:
                    return False
                if node in vis:
                    return
                vis.append(node)
                for i in abj[node]:
                    if dfs(i):
                        return True
                return False
            return dfs(start)
        res=[]
        for start,end in queries:
            if start in abj and div(start,end):
                res.append(True)
            else:
                res.append(False)
        return res
        