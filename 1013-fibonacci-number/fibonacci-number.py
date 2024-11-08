class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        prev1, prev2 = 1, 1
        total = 2
        for _ in range(n-2):
            total = prev1 + prev2
            prev2 = prev1
            prev1 = total
        return total