class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        l,r = 0, len(skill) - 1
        skill.sort()
        targetSkill = skill[l] + skill[r]
        chemistry = 0
        while l < r:
            if skill[l] + skill[r] == targetSkill:
                chemistry += skill[l] * skill[r]
                l += 1
                r -= 1
            else:
                return -1
        return chemistry
            
