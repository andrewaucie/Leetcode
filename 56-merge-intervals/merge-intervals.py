class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        lastInterval = list(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] <= lastInterval[1]:
                lastInterval[1] = max(lastInterval[1], intervals[i][1])
            else:
                res.append(lastInterval)
                lastInterval = list(intervals[i])
        res.append(lastInterval)
        return res