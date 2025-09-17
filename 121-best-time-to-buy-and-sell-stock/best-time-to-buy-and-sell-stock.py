class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        profit = 0
        for p in prices:
            minBuy = min(minBuy, p)
            profit = max(profit, p - minBuy)
        return profit