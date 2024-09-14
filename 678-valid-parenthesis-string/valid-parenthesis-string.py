class Solution:
    def checkValidString(self, s: str) -> bool:
        paranthesis = 0
        star = 0
        for p in s:
            if p == "(":
                paranthesis += 1
            elif p == ")":
                if paranthesis == 0:
                    if star > 0:
                        star -= 1
                        paranthesis += 1
                    else:
                        return False
                paranthesis -= 1
            elif p == "*":
                star += 1
        
        paranthesis = 0
        star = 0
        for p in reversed(s):
            if p == ")":
                paranthesis += 1
            elif p == "(":
                if paranthesis == 0:
                    if star > 0:
                        star -= 1
                        paranthesis += 1
                    else:
                        return False
                paranthesis -= 1
            elif p == "*":
                star += 1
        return True