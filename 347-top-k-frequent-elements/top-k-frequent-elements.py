# Python Solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        mp = defaultdict(int)
        for n in nums:
            mp[n] += 1

        for n, c in mp.items():
            buckets[c].append(n)

        ans = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans