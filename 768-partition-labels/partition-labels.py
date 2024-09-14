class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        freq = Counter(s)
        partitionFreq = defaultdict(int)
        partitionSize = 0
        for c in s:
            partitionFreq[c] += 1
            partitionSize += 1
            
            if partitionFreq[c] == freq[c]:
                del partitionFreq[c]

            if len(partitionFreq) == 0:
                res.append(partitionSize)
                partitionSize = 0
                partitionFreq = defaultdict(int)
        return res