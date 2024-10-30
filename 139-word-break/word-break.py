class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        cache = {}
        def dfs(i, curr):
            if i == len(s):
                return curr in wordSet
            if (i, curr) in cache:
                return cache[(i, curr)]
            skipWord = dfs(i+1, curr + s[i])
            takeWord = (curr in wordSet) and dfs(i+1, s[i])
            cache[(i,curr)] = skipWord or takeWord
            return cache[(i,curr)]
        return dfs(0,"")

