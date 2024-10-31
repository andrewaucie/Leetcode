class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # amount = 5
        # [0,1,2,3,4,5]
        # [0,0,0,0,0,0]
        # [1,2,5]
        # cache = {}
        # def dfs(total):
        #     if total == amount:
        #         return 1
        #     if total in cache:
        #         return cache[total]
        #     combinations = 0
        #     for coin in coins:
        #         for k in range(amount):
        #             if total + coin*k > amount:
        #                 break
        #             combinations += dfs(total + coin*k)
        #     cache[total] = combinations
        #     return cache[total]
        # return dfs(0)

        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for v in range(coin, amount+1):
                dp[v] += dp[v - coin]
        return dp[-1]