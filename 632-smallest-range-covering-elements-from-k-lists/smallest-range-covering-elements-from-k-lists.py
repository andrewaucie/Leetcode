class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        events = []
        for i in range(len(nums)):
            for n in nums[i]:
                events.append((n, i))
        events.sort()
        ranges = {}
        start = float('-inf')
        minRange = [float('-inf'), float('inf')]
        for n, rangeNum in events:
            ranges[rangeNum] = n
            start = min(ranges.values())
            if len(ranges) == len(nums):
                if n - start < minRange[1] - minRange[0]:
                    minRange = [start, n]
        return minRange 