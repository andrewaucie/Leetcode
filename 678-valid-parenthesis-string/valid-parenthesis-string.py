class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}
        def backtrack(i, p):
            if p < 0:
                return False
            if i == len(s):
                return p == 0
            if (i, p) in memo:
                return memo[(i, p)]
            left, right, star = False, False, False
            if s[i] == "(":
                left = backtrack(i+1, p+1)
            elif s[i] == ")":
                right = backtrack(i+1, p-1)
            else:
                star = backtrack(i+1, p+1) or backtrack(i+1, p-1) or backtrack(i+1, p)
            memo[(i,p)] = left or right or star
            return left or right or star
        return backtrack(0,0)