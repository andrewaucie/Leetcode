class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # [1,2,3,6,2,3,4,7,8]
        freq = Counter(hand)
        sortedHands = []
        for key in sorted(freq.keys()):
            sortedHands.append([key, freq[key]])
        
        for i in range(len(sortedHands) - groupSize + 1):
            if sortedHands[i][1] == 0:
                continue
            for j in range(i+1, i+groupSize):
                if (sortedHands[j-1][0] + 1 == sortedHands[j][0] and sortedHands[j][1] >= sortedHands[i][1]):
                    sortedHands[j][1] -= sortedHands[i][1]
                else:
                    return False
            sortedHands[i][1] = 0
        return all(sortedHands[i][1] == 0 for i in range(len(sortedHands)))

        # [(1: 1), (2: 2), (3: 2), (4: 1), (6: 1), (7: 1), (8: 1)]

