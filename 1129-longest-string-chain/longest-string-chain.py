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

        memo = [[-1] * (len(words)) for _ in range(len(words))]

        def memoization(i, j):
            if i == len(words):
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            # Include
            include = 0
            if i != j and checkPred(i,j):
                include = memoization(i+1, i) + 1
            # Exclude
            exclude = memoization(i+1, j)
            memo[i][j] = max(include, exclude)
            return memo[i][j]
        words.sort(key=lambda x:len(x))
        maxLen = 0
        for i in range(len(words)):
            maxLen = max(maxLen, memoization(i, i)+1)
        return maxLen