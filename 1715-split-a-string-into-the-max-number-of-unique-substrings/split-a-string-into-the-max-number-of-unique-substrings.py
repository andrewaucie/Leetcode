class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        def backtrack(i, string):
            if i == len(s):
                return 0
            string += s[i]
            reset = 0
            if string not in seen:
                seen.add(string)
                reset = backtrack(i+1, "") + 1
                seen.remove(string)
            add = backtrack(i+1, string)
            return max(reset, add)
        return backtrack(0, "")
