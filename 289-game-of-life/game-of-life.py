class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # above and left
        prevCells = {(-1,1),(-1,0),(-1,-1),(0,-1)}
        belowRow = {(1,1),(1,0),(1,-1)}
        # store row above
        prevLevel = set()
        for i in range(len(board)):
            currLevel = set()
            for j in range(len(board[0])):
                liveNeighbors = 0
                # check above row, left
                for dx,dy in prevCells:
                    liveNeighbors += int((i+dx,j+dy) in prevLevel)

                # check right
                liveNeighbors += int(j < len(board[0])-1 and board[i][j+1])
    
                # check below row
                for dx,dy in belowRow:
                    if 0 <= i+dx < len(board) and 0 <= j+dy < len(board[0]):
                        liveNeighbors += board[i+dx][j+dy]

                # add to currLevel
                if board[i][j] == 1:
                    prevLevel.add((i,j))
                    currLevel.add((i,j))
                    
                    if liveNeighbors < 2 or liveNeighbors > 3:
                        board[i][j] = 0

                if board[i][j] == 0 and liveNeighbors == 3:
                    board[i][j] = 1

            prevLevel = set(currLevel)
        return