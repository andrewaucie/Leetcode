class Solution:
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        
        dp, g = [1]+[0] * maxLength, gcd(oneGroup,zeroGroup)

        for i in range(1, maxLength + 1):

            if i%g:continue             #<--- no solutions if i%g != 0

            dp[i] += ((dp[i - oneGroup ] if i >= oneGroup  else 0)+
                      (dp[i - zeroGroup] if i >= zeroGroup else 0))

            dp[i]%= 1_000_000_007

        return sum(dp[minLength : maxLength + 1]) % 1000000007