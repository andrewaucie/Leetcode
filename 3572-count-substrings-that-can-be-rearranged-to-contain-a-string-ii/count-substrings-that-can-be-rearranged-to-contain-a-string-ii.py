class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        targetFreq = Counter(word2)
        currFreq = defaultdict(int)
        total = 0
        left = 0
        have, need = 0, len(targetFreq)
        for right in range(len(word1)):
            currFreq[word1[right]] += 1
            if targetFreq[word1[right]] == currFreq[word1[right]]:
                have += 1
                while have == need:
                    total += len(word1) - right
                    currFreq[word1[left]] -= 1
                    if targetFreq[word1[left]] > currFreq[word1[left]]:
                        have -= 1
                    left += 1
        return total
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             