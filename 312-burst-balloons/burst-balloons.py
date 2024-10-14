class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # nums = [1] + nums + [1]
        # memo = {}
        # def coins(i, j):
        #     if i > j:
        #         return 0
        #     if (i,j) in memo:
        #         return memo[(i,j)]
        #     res = 0
        #     for k in range(i, j+1):
        #         res = max(res, coins(i, k-1) + coins(k+1,j) + nums[i-1]*nums[k]*nums[j+1])
        #     memo[(i,j)] = res
        #     return res

        nums = [1] + nums + [1]
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        
        for gap in range(len(nums)):
            for left in range(len(nums)-gap):
                right = left + gap
                
                res = 0
                for i in range(left+1, right):
                    coins = nums[left] * nums[i] * nums[right]
                    res = max(res, coins + dp[left][i] + dp[i][right])
                dp[left][right] = res
                
        return dp[0][len(nums)-1]