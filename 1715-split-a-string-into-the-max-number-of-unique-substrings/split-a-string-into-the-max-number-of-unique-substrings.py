class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        def backtrack(i, seen):
            if i == len(s):
                return 0
            unique = 0
            for end in range(i+1, len(s)+1):
                sub = s[i:end]
                if sub not in seen:
                    seen.add(sub)
                    unique = max(unique, backtrack(end, seen) + 1)
                    seen.remove(sub)
            return unique
        return backtrack(0, set())
