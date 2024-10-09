class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        brackets = 0
        add = 0
        for b in s:
            if b == '(':
                brackets += 1
            else:
                if brackets > 0:
                    brackets -= 1
                else:
                    add += 1
        return brackets + add