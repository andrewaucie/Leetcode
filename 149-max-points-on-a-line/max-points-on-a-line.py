class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 1
        for i in range(len(points)):
            x1,y1 = points[i]
            slopeMap = defaultdict(int)
            for j in range(i+1, len(points)):
                x2,y2 = points[j]
                if x1 == x2:
                    slope = float('inf')
                else:
                    slope = (y1-y2) / (x1-x2)
                slopeMap[slope] += 1
                res = max(res, slopeMap[slope] + 1)
        return res