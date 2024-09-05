class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # find total missing amount
        length = len(rolls) + n
        missingAmount = mean * length - sum(rolls)
        if not (1 <= missingAmount / n <= 6):
            return []
        # construct missing rolls
        divisor = missingAmount // n
        remainder = missingAmount % n
        missing = []
        for _ in range(n):
            missing.append(divisor)
        for i in range(remainder):
            missing[i] += 1
        return missing