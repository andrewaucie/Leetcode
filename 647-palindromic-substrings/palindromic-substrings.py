class Solution:
    def countSubstrings(self, s: str) -> int:
        # Brute force
        # def isPalindrome(left, right):
        #     while left <= right and s[left] == s[right]:
        #         left += 1
        #         right -= 1
        #     return left > right
        
        # res = 0
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         if isPalindrome(i,j):
        #             res += 1
        # return res

        # Expand around centers
        def expand(left, right):
            c = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                c += 1
            return c

        res = 0
        for i in range(len(s)):
            odd = expand(i,i)
            even = expand(i, i+1)
            res += even + odd
        return res

        if len(s) == 1:
            return 1
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            if i < len(s)-1:
                dp[i][i+1] = True
        count = len(s)
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    count += 1
        return count
        
            