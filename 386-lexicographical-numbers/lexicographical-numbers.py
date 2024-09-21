class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        numberGraph = defaultdict(list)
        for i in range(n, 0, -1):
            numberGraph[i // 10].append(i)
        
        res = []
        def dfs(i):
            res.append(i)

            for nextN in reversed(numberGraph[i]):
                dfs(nextN)
            return
        dfs(0)
        return res[1:]