class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        targetA, targetB, targetC = False, False, False
        for triple in triplets:
            if triple[0] == target[0] and triple[1] <= target[1] and triple[2] <= target[2]:
                targetA = True
            if triple[0] <= target[0] and triple[1] == target[1] and triple[2] <= target[2]:
                targetB = True
            if triple[0] <= target[0] and triple[1] <= target[1] and triple[2] == target[2]:
                targetC = True
        return targetA and targetB and targetC