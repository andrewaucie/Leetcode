class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        memo = [-1] * len(s)
        def backtrack(i):
            if i == len(s):
                return 0
            if memo[i] != -1:
                return memo[i]
            minExtra = backtrack(i+1) + 1
            for j in range(i, len(s)):
                curr = s[i:j+1]
                if curr in dictionary:
                    minExtra = min(minExtra, backtrack(j+1))
            memo[i] = minExtra
            return memo[i]
        return backtrack(0)