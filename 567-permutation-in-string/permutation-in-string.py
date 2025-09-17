class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = collections.Counter(s1)
        freq2 = collections.defaultdict(int)
        left = 0
        for right in range(len(s2)):
            freq2[s2[right]] += 1
            while left < right and freq2[s2[left]] > freq1[s2[left]]:
                freq2[s2[left]] -= 1
                if freq2[s2[left]] == 0:
                    del freq2[s2[left]]
                left += 1
            if freq1 == freq2:
                return True
        return False