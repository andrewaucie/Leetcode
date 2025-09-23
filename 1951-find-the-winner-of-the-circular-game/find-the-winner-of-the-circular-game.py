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

        circle = deque(range(1, n+1))
        while len(circle) > 1:
            for _ in range(k-1):
                circle.append(circle.popleft())
            circle.popleft()
        return circle[0]