class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        # BFS, add jump combinations to graph until we reach x
        visited = set()
        forbidden = set(forbidden)
        queue = deque()
        queue.append((0,1,0))
        limit = max(x, max(forbidden)) + a + b
        while queue:
            pos, direction, jumps = queue.popleft()
            if ((pos,direction) in visited) or (pos in forbidden) or pos > limit:
                continue
            visited.add((pos, direction))
            if pos == x:
                return jumps
            # If previous forward jump, can jump forward/back
            # If previous backward jump, can only jump forward
            queue.append((pos+a, 1, jumps+1))
            if direction == 1 and pos > b:
                queue.append((pos-b, -1, jumps+1))
        return -1
            
            
