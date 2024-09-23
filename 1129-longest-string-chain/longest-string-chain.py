class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
    
        dp = {}
        maxChainLength = 0
        
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                pred = word[:i] + word[i+1:]
                if pred in dp:
                    dp[word] = max(dp[word], dp[pred] + 1)
            maxChainLength = max(maxChainLength, dp[word])
        
        return maxChainLength