class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        memo = {}
        def memoization(k, n):
            if n == 0 or n == 1 or k == 1:
                return n
            if (k,n) in memo:
                return memo[(k,n)]
            minAttempts = float('inf')
            l,r = 1, n
            while l <= r:
                mid = (l+r) // 2
                # break, go down
                down = memoization(k-1, mid-1)
                # no break, go up
                up = memoization(k, n-mid)
                temp = max(down,up) + 1
                if down < up:
                    l = mid + 1
                else:
                    r = mid - 1
                minAttempts = min(minAttempts, temp)
            memo[(k,n)] = minAttempts
            return minAttempts
        return memoization(k,n)
