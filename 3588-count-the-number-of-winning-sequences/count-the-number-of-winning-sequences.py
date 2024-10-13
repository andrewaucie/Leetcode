class Solution:
    def countWinningSequences(self, s: str) -> int:
        combat = {
            'E': 'F',
            'W': 'E',
            'F': 'W'
        }
        n = len(s)
        memo = {}
        def backtrack(i, points, prev):
            if i == n:
                return int(points > 0)
            if points + (n - i + 1) < 0:
                return 0
            if (i, points, prev) in memo:
                return memo[(i, points, prev)]
            ways = 0
            for dragon in {'E', 'W', 'F'} - {prev}:
                curr = points
                if combat[s[i]] == dragon:
                    curr += 1
                elif combat[dragon] == s[i]:
                    curr -= 1
                ways += backtrack(i+1, curr, dragon)
            memo[(i, points, prev)] = ways % (10**9 + 7)
            return memo[(i, points, prev)]
        return backtrack(0, 0, '')