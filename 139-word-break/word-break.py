class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        cache = {}
        def dfs(i):
            if i == len(s):
                return True
            if i in cache:
                return cache[i]
            takeWord = False
            for j in range(i, len(s)):
                if s[i:j+1] in wordSet:
                    takeWord |= dfs(j+1)
            cache[i] = takeWord
            return cache[i]
        return dfs(0)

