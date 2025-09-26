class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = costs[0]
        for i in range(1, len(costs)):
            prev = dp[:]
            dp[0] = min(prev[1], prev[2]) + costs[i][0]
            dp[1] = min(prev[0], prev[2]) + costs[i][1]
            dp[2] = min(prev[0], prev[1]) + costs[i][2]
        return min(dp)