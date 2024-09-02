class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        if k > total:
            k %= total
        for i in range(len(chalk)):
            k -= chalk[i]
            if k < 0:
                return i
        return 0