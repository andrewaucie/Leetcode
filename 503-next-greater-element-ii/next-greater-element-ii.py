class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # [1,2,1]
        
        res = [-1] * len(nums)
        stack = []
        index = 0
        while index < len(nums)*2:
            i = index % len(nums)
            while stack and nums[i] > stack[-1][0]:
                res[stack.pop()[1]] = nums[i]
            if stack and (nums[i], i) == stack[-1]:
                return res
            stack.append((nums[i], i))
            index += 1
        return res
        