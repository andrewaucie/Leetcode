class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        count = 0
        total = 0
        for i in range(1, n+1):
            if i not in banned:
                count += 1
                total += i
            if total > maxSum:
                return count - 1
        return count