'''
Brute Force
1. Run dfs from each empty room.
2. keep exploring neighbors and check if it's door or block.
    if block backtrack
    if door, check running count and update the rooms[row][col] = min(rooms[row][col], running_count)
3. 
'''
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        ROW, COL = len(rooms), len(rooms[0])

        visited = set()

        def get_nbr(row, col):
            result = []

            if row-1>=0:
                result.append((row-1, col))
            if col-1>=0:
                result.append((row, col-1))
            if row+1 < ROW:
                result.append((row+1, col))
            if col+1 < COL:
                result.append((row, col+1))

            return result

        def bfs(row, col):
            q = collections.deque([(row, col, 1)])
            count = 0
            visited = set()
            while q:
                node_row, node_col, count = q.popleft()

                for nbr_row, nbr_col in get_nbr(node_row, node_col):
                    if (nbr_row, nbr_col) not in visited:
                        visited.add((nbr_row, nbr_col))
                        if rooms[nbr_row][nbr_col] > 0:
                            rooms[nbr_row][nbr_col] = min(rooms[nbr_row][nbr_col], count)
                            q.append((nbr_row, nbr_col, count+1))
            return

        for row in range(ROW):
            for col in range(COL):
                if rooms[row][col] == 0:
                    bfs(row, col)
        return