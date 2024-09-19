class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # Check if placing 'k' at position (r, c) is valid
        def isValid(r, c, k):
            for i in range(9):
                if board[i][c] == k or board[r][i] == k:
                    return False
                subgrid_row = 3 * (r // 3) + i // 3
                subgrid_col = 3 * (c // 3) + i % 3
                if board[subgrid_row][subgrid_col] == k:
                    return False
            return True    

        def fill(r, c):
            if r == 9:
                return True
            
            if c == 9:
                return fill(r + 1, 0)

            if board[r][c] == '.':
                for k in range(1, 10):
                    if isValid(r, c, str(k)):
                        board[r][c] = str(k)
                        if fill(r, c + 1):
                            return True
                        board[r][c] = '.'
                return False
            return fill(r, c + 1)

        fill(0, 0)