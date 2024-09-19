class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        memo = [[-1] * (len(nums2)+1) for _ in range(len(nums1)+1)]
        def backtrack(i, j):
            if i == 0 or j == 0:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            matched = 0
            if nums1[i-1] == nums2[j-1]:
                matched = backtrack(i-1, j-1) + 1
            memo[i][j] = matched
            return memo[i][j]
        maxLen = 0
        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                maxLen = max(maxLen, backtrack(i,j))
        return maxLen
