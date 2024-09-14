class Solution:
    def checkValidString(self, s: str) -> bool:
        paranthesis = star = 0
        for p in s:
            if p == "(":
                paranthesis += 1
            elif p == ")":
                if paranthesis == 0:
                    return False
                paranthesis -= 1
            elif p == "*":
                paranthesis += 1

        paranthesis = star = 0
        for p in reversed(s):
            if p == ")":
                paranthesis += 1
            elif p == "(":
                if paranthesis == 0:
                    return False
                paranthesis -= 1
            elif p == "*":
                paranthesis += 1
        return True