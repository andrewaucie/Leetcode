class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, comb, combSum):
            if combSum == target:
                res.append(comb.copy())
                return
            if combSum > target or index >= len(candidates):
                return
            comb.append(candidates[index])
            dfs(index, comb, combSum + candidates[index])
            comb.pop()
            dfs(index+1, comb, combSum)
        dfs(0, [], 0)
        return res