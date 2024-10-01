class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainderList = [n%k for n in arr]
        remainders = Counter(remainderList)
        for r in remainderList:
            if k - r in remainders or (r == 0 and remainders[r] >= 2):
                remainders[r] -= 1 + int(r == 0)
                if remainders[k-r] > 0:
                    remainders[k-r] -= 1
                if remainders[r] == 0:
                    del remainders[r]
                if k-r in remainders and remainders[k-r] == 0:
                    del remainders[k-r]
        return len(remainders) == 0
