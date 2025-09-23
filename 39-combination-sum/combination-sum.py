class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        def recurse(i, total):
            if total >= target:
                if total == target:
                    res.append(curr[:])
                return
            if i == len(candidates):
                return
            curr.append(candidates[i])
            recurse(i, total + candidates[i])
            curr.pop()
            recurse(i+1, total)
        recurse(0,0)
        return res