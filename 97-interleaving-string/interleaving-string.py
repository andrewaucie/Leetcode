class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        memo = {}
        def memoization(i1, i2, i3):
            if i3 == len(s3) and i1 == len(s1) and i2 == len(s2):
                return True
            if i3 == len(s3) or (i1 == len(s1) and i2 == len(s2)):
                return False
            if (i1,i2,i3) in memo:
                return memo[(i1,i2,i3)]
            include1, include2 = False, False
            if i1 < len(s1) and s1[i1] == s3[i3]:
                include1 = memoization(i1+1, i2, i3+1)
            if i2 < len(s2) and s2[i2] == s3[i3]:
                include2 = memoization(i1, i2+1, i3+1)
            memo[(i1,i2,i3)] = include1 or include2
            return memo[(i1,i2,i3)]
        return memoization(0,0,0)