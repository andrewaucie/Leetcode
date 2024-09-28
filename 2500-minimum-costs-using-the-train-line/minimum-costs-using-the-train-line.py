class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:        
        # dp
        res = []
        dp = [[float('inf')]*2 for _ in range(len(regular)+1)]
        dp[0][0] = 0
        dp[0][1] = expressCost
        for i in range(1, len(regular)+1):
            dp[i][0] = min(
                dp[i-1][0] + regular[i-1], # stay
                dp[i-1][1] + express[i-1] # switch
            )
            dp[i][1] = min(
                dp[i-1][1] + express[i-1], # stay
                dp[i-1][0] + regular[i-1] + expressCost # switch
            )
            res.append(min(dp[i]))
        return res