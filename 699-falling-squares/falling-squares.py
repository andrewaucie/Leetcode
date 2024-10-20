class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        heights = []
        maxHeight = 0
        res = []

        for left, side in positions:
            right = left + side
            height = 0
            for l, r, h in heights:
                if left < r and right > l:
                    height = max(height, h)
            height += side
            heights.append((left, right, height))
            maxHeight = max(maxHeight, height)
            res.append(maxHeight)
        return res