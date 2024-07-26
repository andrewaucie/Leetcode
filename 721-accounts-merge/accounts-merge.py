class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adjList = defaultdict(set)
        for account in accounts:
            for i,j in combinations(range(1, len(account)), 2):
                adjList[account[i]].add(account[j])
                adjList[account[j]].add(account[i])

        visited = defaultdict(bool)
        def bfs(visited, account):
            queue = deque()
            for i in range(1, len(account)):
                if visited[account[i]] is False:
                    queue.append(account[i])
                    visited[account[i]] = True
            account = [account[0]]
            while queue:
                curr = queue.popleft()
                account.append(curr)
                for e in adjList[curr]:
                    if visited[e] is False:
                        visited[e] = True
                        queue.append(e)
            return account
        
        newAccounts = []
        for account in accounts:
            if visited[account[1]] == False:
                mergedAccount = bfs(visited, account)
                mergedAccount = [account[0]] + sorted(mergedAccount[1:])
                newAccounts.append(mergedAccount)
        return newAccounts

