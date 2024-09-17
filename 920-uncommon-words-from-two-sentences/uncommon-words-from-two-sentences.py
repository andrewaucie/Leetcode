class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = Counter(s1.split(" "))
        words2 = Counter(s2.split(" "))
        res = []
        for word, freq in words1.items():
            if freq == 1 and word not in words2:
                res.append(word)

        for word, freq in words2.items():
            if freq == 1 and word not in words1:
                res.append(word)
        return res