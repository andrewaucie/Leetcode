class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefixSums = {0: -1}
        maxLen = 0
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i] if nums[i] == 1 else -1
            if currSum in prefixSums:
                maxLen = max(maxLen, i - prefixSums[currSum])
            else:
                prefixSums[currSum] = i
        return maxLen


# [0,1,1,0,1]
# find max length subarary sum == 0
# prefix(j) - prefix(i) == 0
# prefix(i) = prefix(j)