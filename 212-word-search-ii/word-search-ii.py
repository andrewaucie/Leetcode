class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n = len(board)
        m = len(board[0])
        trie = {}
        curr = trie
        for word in words:
            for letter in word:
                if letter not in curr:
                    curr[letter] = {}
                curr = curr[letter]
            curr['*'] = ''
            curr = trie
        
        res = []
        def dfs(i, j, string, curr, visited):
            if '*' in curr:
                res.append(string)
            for dx, dy in {(1,0), (0,1), (-1,0), (0,-1)}:
                if 0 <= i+dx < n and 0 <= j+dy < m and (i+dx, j+dy) not in visited:
                    if board[i+dx][j+dy] in curr:
                        visited.add((i+dx, j+dy))
                        dfs(i+dx, j+dy, string + board[i+dx][j+dy], curr[board[i+dx][j+dy]], visited)
                        visited.remove((i+dx, j+dy))
        for i in range(n):
            for j in range(m):
                if board[i][j] in trie:
                    visited = set([(i,j)])
                    dfs(i, j, board[i][j], trie[board[i][j]], visited)
        return set(res)