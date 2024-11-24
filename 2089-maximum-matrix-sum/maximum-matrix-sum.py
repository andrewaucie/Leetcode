class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        minAbsVal = float('inf')
        negCount = 0
        maxSum = 0
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                negCount += int(matrix[i][j] < 0)
                maxSum += abs(matrix[i][j])
                minAbsVal = min(minAbsVal, abs(matrix[i][j]))
        if negCount%2 == 1:
            maxSum -= 2 * minAbsVal
        return maxSum