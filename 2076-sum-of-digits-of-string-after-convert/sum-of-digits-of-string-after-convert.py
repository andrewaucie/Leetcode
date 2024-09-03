class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_str = ''
        for c in s:
            num_str += str(ord(c) - ord('a') + 1)
        next_num = 0
        for _ in range(k):
            next_num = sum(int(c) for c in num_str)
            num_str = str(next_num)
            if len(num_str) == 1:
                break
        return next_num