class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        pointMap = defaultdict(set)
        for x,y in points:
            pointMap[x].add(y)

        minArea = float('inf')
        for x1,y1 in points:
            for x2,y2 in points:
                if x1 != x2 and y1 != y2:
                    if y2 in pointMap[x1] and y1 in pointMap[x2]:
                        minArea = min(minArea, abs(x1-x2) * abs(y1-y2))
        return minArea if minArea != float('inf') else 0