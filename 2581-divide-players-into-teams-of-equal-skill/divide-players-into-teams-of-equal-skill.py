class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        minSkill, maxSkill, freq = float('inf'), 0, defaultdict(int)
        for s in skill:
            minSkill = min(minSkill, s)
            maxSkill = max(maxSkill, s)
            freq[s] += 1
        targetSum = minSkill + maxSkill
        chemistry = 0
        for s in skill:
            if freq[targetSum - s] == 0:
                return -1
            freq[targetSum - s] -= 1
            chemistry += s * (targetSum - s)
        return chemistry // 2
            
