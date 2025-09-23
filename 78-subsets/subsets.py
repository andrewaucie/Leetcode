class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        def recurse(i):
            if i == len(nums):
                res.append(sub[:])
                return
            sub.append(nums[i])
            recurse(i+1)
            sub.pop()
            recurse(i+1)
        recurse(0)
        return res
            