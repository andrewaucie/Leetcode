class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        should_preserve = set()
        m = len(board)
        n = len(board[0])

        def preserve_connected(i, j, visited=None):
            if visited is None:
                visited = set([(i, j)])
            sur = ((0, 1), (0, -1), (1, 0), (-1, 0))
            for di, dj in sur:
                ci, cj = di + i, dj + j
                if 0 < ci < m-1 and 0 < cj < n-1 and (ci, cj) not in visited and board[ci][cj] == 'O':
                    if (ci, cj) in should_preserve:
                        continue
                    should_preserve.add((ci, cj))
                    preserve_connected(ci, cj, visited.union([(ci, cj)]))

        for i in [0, m-1]:
            for j in range(n):
                if board[i][j] == 'O':
                    should_preserve.add((i, j))
                    preserve_connected(i, j)

        for j in [0, n-1]:
            for i in range(1, m-1):
                if board[i][j] == 'O':
                    should_preserve.add((i, j))
                    preserve_connected(i, j)

        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O' and (i, j) not in should_preserve:
                    board[i][j] = 'X'