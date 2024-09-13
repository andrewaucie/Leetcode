class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        memo = [[-1] * (len(word2) + 1) for _ in range(len(word1)+1)]
        def memoization(i1, i2):
            if i1 == len(word1):
                return len(word2) - i2
            if i2 == len(word2):
                return len(word1) - i1
            if memo[i1][i2] != -1:
                return memo[i1][i2]
            if word1[i1] == word2[i2]:
                return memoization(i1+1, i2+1)
            insert = memoization(i1, i2+1)
            delete = memoization(i1+1, i2)
            replace = memoization(i1+1, i2+1)
            memo[i1][i2] = min(delete, replace, insert) + 1
            return memo[i1][i2]

        return memoization(0,0)