class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0]*(k+1) for _ in range(n+1)]
        
        attempts = 0

        while dp[attempts][k] < n:
            attempts += 1
            for eggs in range(1, k+1):
                dp[attempts][eggs] = dp[attempts-1][eggs-1] + dp[attempts-1][eggs] + 1
        return attempts