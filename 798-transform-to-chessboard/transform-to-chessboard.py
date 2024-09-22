class Solution:
    def movesToChessboard(self, board):
        n = len(board)
        pat1, pat2 = [i % 2 for i in range(n)], [(i + 1) % 2 for i in range(n)]
        visited = [[False] * n for _ in range(n)]
        rowSwaps = colSwaps = 0
        
        for i in range(n):
            rowCount = colCount = 0
            for j in range(n):
                rowCount += board[i][j]
                colCount += board[j][i]
                if not visited[i][j]:
                    queue = [(i, j)]
                    visited[i][j] = True
                    val = board[i][j]
                    minRow = maxRow = i
                    minCol = maxCol = j
                    cells = 0
                    while queue:
                        x, y = queue.pop()
                        cells += 1
                        minRow, maxRow = min(minRow, x), max(maxRow, x)
                        minCol, maxCol = min(minCol, y), max(maxCol, y)
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            newX, newY = x + dx, y + dy
                            if 0 <= newX < n and 0 <= newY < n and not visited[newX][newY] and board[newX][newY] == val:
                                visited[newX][newY] = True
                                queue.append((newX, newY))
                    if (maxRow - minRow + 1) * (maxCol - minCol + 1) != cells:
                        return -1

            if n % 2 == 0:
                if rowCount != n // 2 or colCount != n // 2:
                    return -1
            else:
                if not (rowCount in {n // 2, n // 2 + 1}) or not (colCount in {n // 2, n // 2 + 1}):
                    return -1

            if i == 0:
                rowSwaps = self.countSwaps(board[0], pat1, pat2)
                colSwaps = self.countSwaps([board[k][0] for k in range(n)], pat1, pat2)
                if rowSwaps == float('inf') or colSwaps == float('inf'):
                    return -1

        return rowSwaps + colSwaps

    def countSwaps(self, row, pat1, pat2):
        n = len(row)
        mismatch1 = sum(1 for i in range(n) if row[i] != pat1[i])
        mismatch2 = sum(1 for i in range(n) if row[i] != pat2[i])
        return min(mismatch1 // 2 if mismatch1 % 2 == 0 else float('inf'),
                   mismatch2 // 2 if mismatch2 % 2 == 0 else float('inf'))