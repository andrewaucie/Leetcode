class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq = defaultdict(int)
        steps = 0
        for c in s:
            freq[c] += 1
        for c in t:
            if freq[c] == 0:
                steps += 1
            else:
                freq[c] -= 1
        return steps