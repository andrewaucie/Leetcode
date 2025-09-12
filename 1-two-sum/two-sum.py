class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i + j == k
        # i == k - j

        numDict = {}
        for i in range(len(nums)):
            k = target - nums[i]
            if k in numDict:
                return [numDict[k], i]
            numDict[nums[i]] = i
        return []