class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return 0

        # pre-filling of 'saferty'-matrix
        step = 1
        right = len(grid) -1
        deq = deque((i, j) for j in range(len(grid)) for i in range(len(grid)) if grid[i][j] == 1)
        while deq:
            step += 1
            for _ in range(len(deq)):
                i, j = deq.popleft()
                if i > 0 and grid[i-1][j] == 0:
                    deq.append((i-1, j))
                    grid[i-1][j] = step
                if j > 0 and grid[i][j-1] == 0:
                    deq.append((i, j-1))
                    grid[i][j-1] = step
                if i < right and grid[i+1][j] == 0:
                    deq.append((i+1, j))
                    grid[i+1][j] = step
                if j < right and grid[i][j+1] == 0:
                    deq.append((i, j+1))
                    grid[i][j+1] = step

        right = -right
        used = set()
        heap = [(-grid[0][0], 0, 0)]
        while heap:
            dist, i, j = heappop(heap)
            if (i, j) in used:
                continue
            
            if dist < (tmp := -grid[-i][-j]):
                dist = tmp

            used.add((i, j))
            
            if i == j == right:    # thay all are negative
                break

            if i < 0:
                heappush(heap, (dist, i + 1, j))
            if j < 0:
                heappush(heap, (dist, i, j + 1))
            if i > right:
                heappush(heap, (dist, i - 1, j))
            if j > right:
                heappush(heap, (dist, i, j - 1))

        return -dist - 1
 