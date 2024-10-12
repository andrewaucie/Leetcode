class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        x = sum(pos[0] for pos in positions) / len(positions)
        y = sum(pos[1] for pos in positions) / len(positions)
        
        ans = self.euclidanDistance(positions, x, y)
        change = 100
        while change > 1e-6:
            zoom = True
            for dx, dy in (-1, 0), (0, -1), (1, 0), (0, 1):
                xx = x + change*dx
                yy = y + change*dy
                dd = self.euclidanDistance(positions, xx, yy)
                if dd < ans:
                    ans = dd
                    x = xx
                    y = yy
                    zoom = False
                    break
            if zoom:
                change /= 2
        return ans
    
    def euclidanDistance(self, positions, x, y):
        return sum(sqrt((x-xx)**2 + (y-yy)**2) for xx, yy in positions)