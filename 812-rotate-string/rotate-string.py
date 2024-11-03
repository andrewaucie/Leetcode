class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        n = len(s)
        for start in range(n):
            valid = True
            for j in range(start, n + start):
                if s[j - start] != goal[j % n]:
                    valid = False
                    break
            if valid:
                return True
        return False