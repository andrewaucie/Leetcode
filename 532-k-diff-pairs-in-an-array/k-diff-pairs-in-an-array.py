class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # | nums[i] - nums[j] | = k => nums[i] = nums[j] + k or nums[j] - k
        # create numsSet
        # at index i, check if nums[j] + k exists in numsSet
        # if exists, mark (nums[i], nums[j]) as set
        indexMap = {nums[i]: i for i in range(len(nums))}
        pairs = 0
        visitedPairs = set()
        for i in range(len(nums)):
            if nums[i] + k in indexMap and indexMap[nums[i]+k] != i:
                sortedTuple = tuple(sorted([nums[i], nums[i]+k]))
                if sortedTuple not in visitedPairs:
                    visitedPairs.add(sortedTuple)
        return len(visitedPairs)