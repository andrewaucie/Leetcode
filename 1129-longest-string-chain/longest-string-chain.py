class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def checkPred(i,j):
            prev, curr = 0, 0
            while prev < len(words[j]) and curr < len(words[i]) and words[j][prev] == words[i][curr]:
                prev += 1
                curr += 1
            curr += 1
            while prev < len(words[j]) and curr < len(words[i]) and words[j][prev] == words[i][curr]:
                prev += 1
                curr += 1
            return curr == len(words[i]) and prev == len(words[j])

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