class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Memoization
        # memo = [[-1] * len(coins) for _ in range(amount+1)]
        # def memoization(i, k):
        #     if i == len(coins) or k < 0:
        #         return 0
        #     if k == 0:
        #         return 1
        #     if memo[k][i] != -1:
        #         return memo[k][i]
        #     add = memoization(i, k - coins[i])
        #     skip = memoization(i+1, k)
        #     memo[k][i] = add + skip
        #     return memo[k][i]
        # return memoization(0, amount)

        # DP
        dp = [[0] * (amount+1) for _ in range(len(coins)+1)]
        for i in range(len(coins)+1):
            dp[i][0] = 1
        for i in range(len(coins)-1, -1, -1):
            for k in range(1, amount+1):
                dp[i][k] = dp[i+1][k]
                if k >= coins[i]:
                    dp[i][k] += dp[i][k - coins[i]]
        return dp[0][amount]