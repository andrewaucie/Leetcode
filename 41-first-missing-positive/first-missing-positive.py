class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        firstPositive = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                firstPositive = i
                break
        visited = set()
        k = 1
        for i in range(firstPositive, len(nums)):
            if nums[i] not in visited:
                if nums[i] != k:
                    return k
                visited.add(nums[i])
                k += 1
        return k