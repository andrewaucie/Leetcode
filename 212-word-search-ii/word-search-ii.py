class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n = len(board)
        m = len(board[0])
        trie = {}
        for word in words:
            curr = trie
            for letter in word:
                if letter not in curr:
                    curr[letter] = {}
                curr = curr[letter]
            curr['*'] = word
        
        res = []
        def backtracking(i, j, curr):
            letter = board[i][j]
            if '*' in curr:
                res.append(curr.pop('*'))
            board[i][j] = '#'
            for dx, dy in {(1,0), (0,1), (-1,0), (0,-1)}:
                if 0 <= i+dx < n and 0 <= j+dy < m:
                    if board[i+dx][j+dy] in curr:
                        backtracking(i+dx, j+dy, curr[board[i+dx][j+dy]])
            board[i][j] = letter
            if curr == {}:
                del curr

        for i in range(n):
            for j in range(m):
                if board[i][j] in trie:
                    backtracking(i, j, trie[board[i][j]])
        return res