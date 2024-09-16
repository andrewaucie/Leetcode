class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def backtrack(string, pattern):
            if string == -1 and pattern == -1:
                return True
            if pattern == -1:
                return False
            if (string, pattern) in memo:
                return memo[(string, pattern)]
            if string == -1:
                memo[(string, pattern)] = (p[pattern] == "*" and backtrack(string, pattern-1))
                return memo[(string, pattern)]
            if s[string] == p[pattern] or p[pattern] == '?':
                memo[(string, pattern)] = backtrack(string-1, pattern-1)
            elif p[pattern] == '*':
                memo[(string, pattern)] = backtrack(string-1, pattern) or backtrack(string, pattern-1)
            else:
                memo[(string, pattern)] = False
            return memo[(string, pattern)]
        return backtrack(len(s)-1, len(p)-1)
                