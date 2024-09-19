class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m,n = len(nums1), len(nums2)
        memo = [[-1] * (n+1) for _ in range(m+1)]

        def longest_common_subarray(i,j):
            if i == 0 or j == 0:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            
            res = 0
            if nums1[i-1] == nums2[j-1]:
                res = 1 + longest_common_subarray(i-1,j-1)
            memo[i][j] = res
            return memo[i][j]

        max_length = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                max_length = max(max_length, longest_common_subarray(i,j))
        return max_length