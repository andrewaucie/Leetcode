class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        dp = [0] * (len(s)+1)
        for i in range(len(s)-1, -1, -1):
            dp[i] = dp[i+1] + 1
            for j in range(i, len(s)):
                curr = s[i:j+1]
                if curr in dictionary:
                    dp[i] = min(dp[i], dp[j+1])
        return dp[0]
