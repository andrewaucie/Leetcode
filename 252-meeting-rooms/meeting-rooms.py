class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) < 2:
            return True
        intervals.sort(key=lambda x: x[1])
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < prevEnd:
                return False
            prevEnd = intervals[i][1]
        return True
