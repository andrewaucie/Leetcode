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
        missing = [divisor] * (n - remainder)
        if remainder != 0:
            for _ in range(remainder):
                missing.append(divisor+1)
        return missing