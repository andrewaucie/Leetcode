class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        maxProfit = 0
        while r < len(prices):
            maxProfit = max(maxProfit, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
        return maxProfit