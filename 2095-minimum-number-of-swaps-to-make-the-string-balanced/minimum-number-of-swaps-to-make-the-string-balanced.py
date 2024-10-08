class Solution:
    def minSwaps(self, s: str) -> int:
        brackets = 0
        swaps = 0
        for b in s:
            if b == '[':
                brackets += 1
            else:
                if brackets == 0:
                    swaps += 1
                else:
                    brackets -= 1
        return (swaps + 1) // 2