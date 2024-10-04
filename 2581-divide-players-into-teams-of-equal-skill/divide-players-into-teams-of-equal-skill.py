class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        minSkill, maxSkill, skillMap = float('inf'), 0, defaultdict(int)
        for s in skill:
            minSkill = min(minSkill, s)
            maxSkill = max(maxSkill, s)
            skillMap[s] += 1
        targetSum = minSkill + maxSkill
        chemistry = 0
        for skill, freq in skillMap.items():
            partnerSkill = targetSum - skill
            if partnerSkill not in skillMap or skillMap[partnerSkill] != freq:
                return -1
            chemistry += skill * (partnerSkill) * freq
        return chemistry // 2
            
