class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = {}
        for word in wordDict:
            curr = trie
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['*'] = True
        # leetcode
        # leet code
        dp = [False] * len(s)
        for i in range(len(s)):
            if i > 0 and not dp[i-1]:
                continue
            curr = trie
            for j in range(i, len(s)):
                if s[j] not in curr:
                    break
                print(s[j])
                curr = curr[s[j]]
                if '*' in curr:
                    dp[j] = True
        return dp[-1]
