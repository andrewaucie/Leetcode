class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Brute Force
        memo = [[-1] * len(coins) for _ in range(amount+1)]
        def memoization(i, k):
            if i == len(coins) or k < 0:
                return 0
            if k == 0:
                return 1
            if memo[k][i] != -1:
                return memo[k][i]
            add = memoization(i, k - coins[i])
            skip = memoization(i+1, k)
            memo[k][i] = add + skip
            return memo[k][i]
        return memoization(0, amount)