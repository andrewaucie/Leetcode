class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        curr = []
        def recurse(i, total):
            if total == target:
                res.append(curr[:])
            if total >= target or i == len(candidates):
                return
            curr.append(candidates[i])
            recurse(i+1, total + candidates[i])
            curr.pop()
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            recurse(i+1, total)
        recurse(0, 0)
        return res