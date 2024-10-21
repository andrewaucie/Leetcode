class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    box[(i // 3, j // 3)].add(board[i][j])
        def backtrack(i,j):
            if j >= len(board):
                i += 1
                j = 0
            if i >= len(board):
                return True
            if board[i][j] != ".":
                return backtrack(i, j+1)
            for n in range(1, 10):
                n = str(n)
                if (n not in rows[i]) and (n not in cols[j]) and (n not in box[(i // 3, j // 3)]):
                    rows[i].add(n)
                    cols[j].add(n)
                    box[(i // 3, j // 3)].add(n)
                    board[i][j] = n
                    if backtrack(i, j+1):
                        return True
                    board[i][j] = "."
                    rows[i].remove(n)
                    cols[j].remove(n)
                    box[(i // 3, j // 3)].remove(n)
            return False
        backtrack(0,0)
        