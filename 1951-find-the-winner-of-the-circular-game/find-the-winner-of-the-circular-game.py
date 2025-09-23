class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # clarify problem description
        # clarify input/output & edge cases
        # run through examples covering edge cases
        # [-1, 2, 3, 4, 5]
        # [1, -3, 4, 5]
        # [1, 3, -5]
        # [-3, 5]
        # [3]
        
        # start at idx, land on idx + k - 1
        # mark nums[idx + k - 1] as 0
        
        # numSet = set(nums)

        # every iteration of the game, increment ptr only if nums[i] in numSet
        # stop when ptr == k:
        #     numSet.remove(nums[ptr])
        #     if len(numSet) == 1:
        #        return numSet[0]

        nums = set([i for i in range(n)])
        ptr = 0
        while len(nums) > 1:
            # traverse k friends
            currK = 1
            while currK < k:
                ptr = (ptr + 1) % n
                if ptr in nums:
                    currK += 1
            # currK == k, remove this num
            nums.remove(ptr)
            # find next valid friend
            while True:
                if ptr in nums:
                    break
                ptr = (ptr + 1) % n
        return nums.pop() + 1
