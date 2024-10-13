class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        events = []
        for i in range(len(nums)):
            for n in nums[i]:
                events.append((n, i))
        events.sort()
        ranges = defaultdict(int)
        minRange = [float('-inf'), float('inf')]
        l = 0
        for r, (n, rangeIndex) in enumerate(events):
            ranges[rangeIndex] += 1

            while len(ranges) == len(nums):
                if n - events[l][0] < minRange[1] - minRange[0]:
                    minRange = [events[l][0], n]

                ranges[events[l][1]] -= 1
                if ranges[events[l][1]] == 0:
                    del ranges[events[l][1]]
                l += 1
        return minRange
