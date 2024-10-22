class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        dp = {}
        def dfs(i, prev):
            if i == len(nums1):
                return 0
            if (i,prev) in dp:
                return dp[(i,prev)]
            res = 0
            if not prev:
                res = dfs(i+1, prev)
            if prev <= nums1[i]:
                res = max(res, 1 + dfs(i+1, nums1[i]))
            if prev <= nums2[i]:
                res = max(res, 1 + dfs(i+1, nums2[i]))
            dp[(i,prev)] = res
            return res
        return dfs(0,0)