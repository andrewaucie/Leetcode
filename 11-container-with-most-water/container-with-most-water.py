class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        # to maximize the area, we want to maximize height/width
        # start at max width, 2 pointer inwards
        maxArea = 0
        while l < r:
            currArea = min(height[l], height[r]) * (r - l)
            maxArea = max(maxArea, currArea)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea
