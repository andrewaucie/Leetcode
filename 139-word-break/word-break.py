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
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            if not dp[i]:
                continue
            curr = trie
            for j in range(i, len(s)):
                if s[j] not in curr:
                    break
                print(s[j])
                curr = curr[s[j]]
                if '*' in curr:
                    dp[j+1] = True
        return dp[-1]
