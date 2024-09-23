class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        slopeMap = defaultdict(set)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1,y1 = points[i]
                x2,y2 = points[j]
                if x1 == x2:
                    slope = float('inf')
                    b = x1
                else:
                    slope = (y1-y2) / (x1-x2)
                    b = y1 - slope * x1
                slopeMap[(slope,b)].add(i)
                slopeMap[(slope,b)].add(j)
        return len(max(slopeMap.values(), key=len)) if slopeMap else 1