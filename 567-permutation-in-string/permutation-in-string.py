class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        targetFreq = Counter(s1)
        currFreq = defaultdict(int)
        l,r = 0,0
        while r < len(s2):
            right = s2[r]
            currFreq[right] += 1
            while l <= r and (right not in targetFreq or currFreq[right] > targetFreq[right]):
                left = s2[l]
                currFreq[left] -= 1
                if currFreq[left] == 0:
                    del currFreq[left]
                l += 1
            if targetFreq == currFreq:
                return True
            r += 1
        return False
