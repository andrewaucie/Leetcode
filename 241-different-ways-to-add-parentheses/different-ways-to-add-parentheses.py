class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        nums, ops = [], []
        i = 0
        while i < len(expression):
            if expression[i].isdigit():
                num = 0
                while i < len(expression) and expression[i].isdigit():
                    num = num * 10 + int(expression[i])
                    i += 1
                nums.append(num)
            else:
                ops.append(expression[i])
                i += 1

        n = len(nums)
        dp = [[[] for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = [nums[i]]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = []
                for k in range(i, j):
                    left_results = dp[i][k]
                    right_results = dp[k + 1][j]
                    operator = ops[k]

                    for left in left_results:
                        for right in right_results:
                            if operator == '+':
                                dp[i][j].append(left + right)
                            elif operator == '-':
                                dp[i][j].append(left - right)
                            else:
                                dp[i][j].append(left * right)

        return dp[0][n - 1]