class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        s1, s2 = 0, 0
        while s1 < len(str1) and s2 < len(str2):
            if 0 <= ord(str2[s2]) - ord(str1[s1]) <= 1 or (str1[s1] == 'z' and str2[s2] == 'a'):
                s2 += 1
            s1 += 1
        return s2 == len(str2)