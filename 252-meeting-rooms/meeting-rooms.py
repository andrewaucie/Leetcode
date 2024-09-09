class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        counts = set()

        for interval in intervals:
            for i in range(interval[0], interval[1]):
                if i not in counts:
                    counts.add(i)
                else:
                    return False
        return True
