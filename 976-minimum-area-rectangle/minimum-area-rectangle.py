class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        pointMap = defaultdict(list)
        for x,y in points:
            pointMap[y].append(x)
        
        pairXMap = defaultdict(list)
        for y in pointMap:
            if len(pointMap[y]) > 1:
                for i in range(len(pointMap[y])):
                    for j in range(i+1, len(pointMap[y])):
                        key = sorted([pointMap[y][i], pointMap[y][j]])
                        pairXMap[tuple(key)].append(y)
        minArea = float('inf')
        for (x1, x2) in pairXMap:
            yPoints = sorted(pairXMap[(x1,x2)])
            if len(yPoints) > 1:
                minDist = float('inf')
                for i in range(1, len(yPoints)):
                    minDist = min(minDist, yPoints[i] - yPoints[i-1])
                minArea = min(minArea, abs((x2-x1)*minDist))
        return minArea if minArea != float('inf') else 0