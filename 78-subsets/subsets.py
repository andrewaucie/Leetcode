class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def recurse(i, sub):
            print(i, sub)
            if i == len(nums):
                res.append(list(sub))
                return
            sub.append(nums[i])
            recurse(i+1, sub)
            sub.pop()
            recurse(i+1, sub)
        recurse(0, [])
        return res
            