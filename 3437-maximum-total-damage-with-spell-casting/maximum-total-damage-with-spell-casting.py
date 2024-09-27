class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = Counter(power)
        power = sorted(set(power))
        damage = {spell: spell*freq[spell] for spell in power}
        dp = [0] * len(power)
        
        for i in range(len(power)):
            prevMax = 0
            j = i - 1
            while j >= 0 and power[i] - power[j] <= 2:
                j -= 1
            if j >= 0:
                prevMax = dp[j]
            dp[i] = max(prevMax + damage[power[i]], dp[i-1])
        return dp[-1]
                