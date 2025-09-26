class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        c = len(nums)-1
        while c >= 0:
            a = 0
            b = c-1
            while a < b:
                if nums[a] + nums[b] > nums[c]:
                    total += b - a
                    b -= 1
                else:
                    a += 1
            c -= 1
        return total