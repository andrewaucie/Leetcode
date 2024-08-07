# Python Solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Create a dictionary (`mp`) to store the frequency of each element in the array.
        # Step 2: Create buckets to store elements based on their frequency.
        buckets = [[] for i in range(len(nums) + 1)]
        mp = {}
        # Step 3: Iterate through the array to populate the `mp` dictionary.
        for n in nums:
            mp[n] = 1 + mp.get(n, 0)

        # Step 4: Iterate through the items in `mp` and distribute elements into the corresponding buckets based on their frequency.
        for n, c in mp.items():
            buckets[c].append(n)

        # Step 5: Iterate through the buckets from right to left (highest to lowest frequency) and append elements to the answer list until the desired k elements are collected.
        ans = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans