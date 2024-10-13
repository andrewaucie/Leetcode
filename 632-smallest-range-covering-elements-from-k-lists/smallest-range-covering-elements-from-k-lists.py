from sortedcontainers import SortedList

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        events = []
        for i in range(len(nums)):
            for n in nums[i]:
                events.append((n, i))
        events.sort()
        ranges = SortedList()
        rangeDict = {}
        start = float('-inf')
        minRange = [float('-inf'), float('inf')]
        for n, rangeNum in events:
            if rangeNum in rangeDict:
                ranges.remove(rangeDict[rangeNum])
            ranges.add(n)
            rangeDict[rangeNum] = n
            if len(ranges) > 1:
                start = ranges[0]
            if len(ranges) == len(nums):
                if n - start < minRange[1] - minRange[0]:
                    minRange = [start, n]
        return minRange if minRange != [float('-inf'), float('inf')] else [nums[0][0], nums[0][0]]