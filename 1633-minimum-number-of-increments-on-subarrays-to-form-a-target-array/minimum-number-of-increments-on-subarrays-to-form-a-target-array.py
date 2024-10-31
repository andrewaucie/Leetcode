class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ops = 0
        prevHeight = 0
        for height in target:
            if height > prevHeight:
                ops += height - prevHeight
            prevHeight = height
        return ops