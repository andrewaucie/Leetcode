class Solution:
    def minSwaps(self, s: str) -> int:
        brackets = 0
        for b in s:
            if b == '[':
                brackets += 1
            else:
                if brackets > 0:
                    brackets -= 1
        return (brackets + 1) // 2