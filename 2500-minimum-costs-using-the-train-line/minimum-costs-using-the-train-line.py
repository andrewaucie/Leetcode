class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        
        # memo = {}
        # def memoization(stop, exp, dest):
        #     if (stop,exp,dest) in memo:
        #         return memo[(stop,exp,dest)]
        #     if stop == dest:
        #         return 0
        #     if exp:
        #         stayCost = express[stop]
        #         switchCost = 0
        #     else:
        #         stayCost = regular[stop]
        #         switchCost = expressCost
        #     stay = memoization(stop+1, exp, dest)
        #     switch = switchCost + memoization(stop+1, not exp, dest)
        #     memo[(stop,exp,dest)] = stayCost + min(stay, switch)
        #     return memo[(stop,exp,dest)]
        
        # res = []
        # for i in range(1, len(regular)+1):
        #     cost = min(memoization(0, False, i), memoization(0, True, i) + expressCost)
        #     res.append(cost)
        
        # dp
        res = []
        dp = [[float('inf')]*2 for _ in range(len(regular)+1)]
        dp[0][0] = 0
        dp[0][1] = expressCost
        for i in range(1, len(regular)+1):
            dp[i][0] = min(
                dp[i-1][0] + regular[i-1],
                dp[i-1][1] + express[i-1]
            )
            dp[i][1] = min(
                dp[i-1][1] + express[i-1],
                dp[i-1][0] + regular[i-1] + expressCost
            )
            res.append(min(dp[i]))
        return res