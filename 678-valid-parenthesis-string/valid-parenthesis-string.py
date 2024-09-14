class Solution:
    def checkValidString(self, s: str) -> bool:
        def checkString(flag, string):
            paranthesis = 0
            for p in string:
                if p == "(":
                    paranthesis += flag
                elif p == ")":
                    paranthesis -= flag
                elif p == "*":
                    paranthesis += 1
                if paranthesis < 0:
                    return False
            return True
        return checkString(1, s) and checkString(-1, reversed(s))