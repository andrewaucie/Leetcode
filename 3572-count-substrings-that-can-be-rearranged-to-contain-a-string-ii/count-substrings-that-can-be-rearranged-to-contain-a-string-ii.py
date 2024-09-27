class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        targetFreq = Counter(word2)
        total = 0
        i = 0
        count = len(word2)
        for c in word1:
            if targetFreq[c] > 0:
                count -= 1
            targetFreq[c] -= 1
            while count == 0:
                if targetFreq[word1[i]] == 0:
                    count += 1
                targetFreq[word1[i]] += 1
                i += 1
            total += i
        return total
        # [b,c,c,a]
        # [a,b,c]
        # 