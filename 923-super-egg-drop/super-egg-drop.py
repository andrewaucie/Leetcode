class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        def ed(e,f,dp):
            if f == 0 or f == 1:
                return f
            if e == 1:
                return f
            if dp[e][f] != -1:
                return dp[e][f]
            mini = 10001
            l = 1
            h = f
            while l<=h:
                k = (l+h)//2
                if dp[e-1][k-1] != -1:
                    low = dp[e-1][k-1]
                else:
                    low = ed(e-1,k-1,dp)
                if dp[e][f-k] != -1:
                    high = dp[e][f-k]
                else:
                    high = ed(e,f-k,dp)
                temp = max(high,low) + 1
                if high > low:
                    l = k+1
                else:
                    h = k-1
                mini = min(mini,temp)
            dp[e][f] = mini
            return mini
        dp = [[-1 for i in range(n+1)] for i in range(k+1)]
        ans = ed(k,n,dp)
        return ans
