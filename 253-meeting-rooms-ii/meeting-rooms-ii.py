class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],x[1]))
        overlapping = list(intervals)
        res = 0
        while overlapping:
            nextOverlapping = []
            prevEnd = overlapping[0][1]
            for i in range(1, len(overlapping)):
                if overlapping[i][0] < prevEnd:
                    nextOverlapping.append(overlapping[i])
                else:
                    prevEnd = overlapping[i][1]
            overlapping = nextOverlapping
            res += 1
        return res    
            