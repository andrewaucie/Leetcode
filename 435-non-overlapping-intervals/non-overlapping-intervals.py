class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        currInterval = 0
        nextInterval = 1
        res = 0
        while nextInterval < len(intervals):
            if intervals[nextInterval][1] < intervals[currInterval][1]:
                currInterval = nextInterval
                res += 1
            elif intervals[nextInterval][0] < intervals[currInterval][1]:
                res += 1
            else:
                currInterval = nextInterval
            nextInterval += 1
        return res
            