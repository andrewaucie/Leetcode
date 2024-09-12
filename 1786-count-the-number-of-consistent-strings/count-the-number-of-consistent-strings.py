class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedChars = set(allowed)
        count = 0
        for word in words:
            consistent = True
            for c in word:
                if c not in allowedChars:
                    count += 1
                    break
        return len(words) - count