class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # [1,2,3,6,2,3,4,7,8]
        n = len(hand)
        if n % groupSize != 0:
            return False

        freq = Counter(hand)
        for key in sorted(freq.keys()):
            if freq[key] > 0:
                count = freq[key]
                for nextKey in range(key, key + groupSize):
                    if nextKey not in freq or freq[nextKey] < count:
                        return False
                    freq[nextKey] -= count
        return True


        # [(1: 1), (2: 2), (3: 2), (4: 1), (6: 1), (7: 1), (8: 1)]

