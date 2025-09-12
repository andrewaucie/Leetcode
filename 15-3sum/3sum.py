class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort
        # [-4, -1, -1, 0, 1, 2]
        # pick each number as k, run 2 pointer to find l + r such that k < l < r
        triples = set()
        nums.sort()
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    triples.add(tuple(sorted([nums[i], nums[l], nums[r]])))
                    l += 1
                    r -= 1
        return list(triples)          