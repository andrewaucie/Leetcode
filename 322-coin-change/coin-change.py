class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Brute Force
        def coinChangeBruteForce(coins, amount):
            n = len(coins)
            mempo = {}
            def dfs(index, amount):
                if amount == 0:
                    return 0
                if index < n and amount > 0:
                    minCost = float('inf')
                    for x in range(0, amount // coins[index] + 1):
                        res = dfs(index+1, amount - x*coins[index])
                        if res != -1:
                            minCost = min(minCost, res+x)
                    return -1 if minCost == float('inf') else minCost
                return -1
            return dfs(0, amount)

        # Recursion
        def coinChangeRecursion(coins, amount):
            if amount == 0:
                return 0
            minCoins = float('inf')
            for coin in coins:
                if amount - coin >= 0:
                    res = coinChangeRecursion(coins, amount - coin)
                    if res >= 0:
                        minCoins = min(minCoins, res + 1)
            return minCoins if minCoins != float('inf') else -1
        # DP
        def coinChangeTabulation(coins, amount):
            dp = [amount + 1] * (amount+1)
            dp[0] = 0
            for a in range(1, amount+1):
                for c in coins:
                    if a - c >= 0:
                        dp[a] = min(dp[a], 1 + dp[a-c])
            return dp[amount] if dp[amount] != amount + 1 else -1
        
        return coinChangeTabulation(coins, amount)