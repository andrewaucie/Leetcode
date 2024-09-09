class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Reverse traverse. If can reach index i, move down index until you reach 0
        goal = len(nums) - 1

        for i in range(len(nums)-2, -1, -1):
            if i+nums[i] >= goal:
                goal = i

        return True if goal == 0 else False
