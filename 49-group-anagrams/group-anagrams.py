class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        freqSet = {}
        i = 0
        for s in strs:
            count = tuple(sorted(Counter(s).items()))
            if count not in freqSet:
                freqSet[count] = i
                res.append([s])
                i += 1
            else:
                res[freqSet[count]].append(s)
        return res
