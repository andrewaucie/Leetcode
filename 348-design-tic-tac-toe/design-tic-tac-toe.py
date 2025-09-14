class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [[0]*n for _ in range(n)]


    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        # check row
        if self.board[row] == [player] * self.n:
            return player
        # check col
        if all(self.board[i][col] == player for i in range(self.n)):
            return player
        # check diag
        if row == col and all(self.board[i][i] == player for i in range(self.n)):
            return player
        # check anti
        if row + col == self.n-1 and all(self.board[i][self.n - i - 1] == player for i in range(self.n)):
            return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)