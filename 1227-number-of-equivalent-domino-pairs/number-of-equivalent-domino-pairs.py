class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)
        for domino in dominoes:
            count[tuple(sorted(domino))] += 1
        return int(sum(dominoSum*(dominoSum-1) / 2 for (domino, dominoSum) in count.items()))
