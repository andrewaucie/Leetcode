class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(index, comb, combSum):
            if combSum == target:
                res.append(comb.copy())
                return
            if combSum > target or index >= len(candidates):
                return
            comb.append(candidates[index])
            backtrack(index+1, comb, combSum + candidates[index])
            comb.pop()
            while index < len(candidates)-1 and candidates[index] == candidates[index+1]:
                index += 1
            backtrack(index+1, comb, combSum)
        
        backtrack(0, [], 0)
        return res