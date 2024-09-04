class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        pos = [0,0]
        obstacles = set((x,y) for [x,y] in obstacles)
        # 0 North, 1 East, 2 South, 3 West
        direction = 0
        maxDistance = 0
        for c in commands:
            maxDistance = max(maxDistance, pos[0]**2 + pos[1]**2)
            if c == -1:
                direction = (direction + 1) % 4
            elif c == -2:
                direction = (direction - 1) % 4
            else:
                if direction == 0:
                    for k in range(pos[1], pos[1]+c+1):
                        if (pos[0], k+1) in obstacles:
                            break
                    pos[1] = k
                elif direction == 2:
                    for k in range(pos[1], pos[1]-c-1, -1):
                        if (pos[0], k-1) in obstacles:
                            break
                    pos[1] = k
                elif direction == 1:
                    for k in range(pos[0], pos[0]+c+1):
                        if (k+1, pos[1]) in obstacles:
                            break
                    pos[0] = k
                elif direction == 3:
                    for k in range(pos[0], pos[0]-c-1, -1):
                        if (k-1, pos[1]) in obstacles:
                            break
                    pos[0] = k
        maxDistance = max(maxDistance, pos[0]**2 + pos[1]**2)
        return maxDistance
                
                