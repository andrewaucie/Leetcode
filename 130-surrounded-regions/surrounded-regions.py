class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs(i,j,captured):
            if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0])-1:
                return False
            captured.add((i,j))
            direction = {(0,1),(1,0),(-1,0),(0,-1)}
            for dx,dy in direction:
                if 0 <= i+dx < len(board) and 0 <= j+dy < len(board[0]) and board[i+dx][j+dy] == "O" and (i+dx,j+dy) not in captured:
                    if not dfs(i+dx,j+dy,captured):
                        return False
            return True
            
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                captured = set()
                if board[i][j] == "O" and dfs(i,j,captured):
                    for (x,y) in captured:
                        board[x][y] = "X"
        return