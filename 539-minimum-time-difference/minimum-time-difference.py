class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        for i in range(len(timePoints)):
            hour, minute = timePoints[i].split(":")
            timePoints[i] = int(hour)*60 + int(minute)
        timePoints.sort()
        minDiff = ((23*60 + 60) - timePoints[-1]) + timePoints[0]
        for i in range(1, len(timePoints)):
            minDiff = min(minDiff, timePoints[i] - timePoints[i-1])
        return minDiff