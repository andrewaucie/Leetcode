class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        phoneMap = {
            "2": {"a", "b", "c"},
            "3": {"d", "e", "f"},
            "4": {"g", "h", "i"},
            "5": {"j", "k", "l"},
            "6": {"m", "n", "o"},
            "7": {"p", "q", "r", "s"},
            "8": {"t", "u", "v"},
            "9": {"w", "x", "y", "z"}
        }
        res = []
        
        def backtrack(i, curr):
            if i == len(digits):
                res.append(curr)
                return
            for c in phoneMap[digits[i]]:
                backtrack(i+1, curr + c)
        backtrack(0, "")
        return res