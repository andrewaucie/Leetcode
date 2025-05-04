class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)
        pairs = 0
        for domino in dominoes:
            key = tuple(sorted(domino))
            pairs += count[key]
            count[key] += 1
        return pairs
