class Solution:
    def countArrangement(self, n: int) -> int:
        # backtrack on perm[i] % i == 0
        # backtrack on i % perm[i] == 0
        nums = set(i for i in range(1, n+1))
        def backtrack(i, arr):
            if i > n:
                return 1
            total = 0
            for num in list(nums):
                if num % i == 0 or i % num == 0:
                    nums.remove(num)
                    total += backtrack(i+1, arr + [num])
                    nums.add(num)
            return total
        return backtrack(1, [])
            