class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(index, subset):
            if index == len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[index])
            dfs(index+1, subset)
            subset.pop()
            while index < len(nums)-1 and nums[index] == nums[index+1]:
                index += 1
            dfs(index+1, subset)
        
        dfs(0, [])
        return res