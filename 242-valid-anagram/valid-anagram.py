class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        wordMap = defaultdict(int)
        for i in s:
            wordMap[i] += 1
        for i in t:
            wordMap[i] -= 1
            if wordMap[i] < 0:
                return False
        return True