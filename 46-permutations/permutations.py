class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(curr, ans):
            if len(curr) == len(nums):
                ans.append(curr)
                return
            for i in nums:
                if i not in curr:
                    dfs(curr + [i], ans)
        dfs([], ans)
        return ans