class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        for left, right in intervals:
            events.append((left, 0))
            events.append((right, 1))
        events.sort()
        minGroups, currGroups = 1, 0
        for n, event in events:
            if event == 0:
                currGroups += 1
            else:
                currGroups -= 1
            minGroups = max(minGroups, currGroups)
        return minGroups