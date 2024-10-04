class Solution:
    def bestClosingTime(self, customers: str) -> int:
        pMax = 0
        iMax = -1
        p = 0
        for i,c in enumerate(customers):
            if c == 'Y':
                p += 1
            elif c == 'N':
                p -= 1
            if p > pMax:
                pMax = p
                iMax = i
        return iMax + 1
