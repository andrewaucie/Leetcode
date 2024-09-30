class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        arr = [bin(num).count('1') for num in set(nums)]
        arr.sort()
        pairs = 0
        l,r = 0, len(arr)-1
        while l <= r:
            if arr[l] + arr[r] >= k:
                pairs += (r - l)*2 + 1
                r -= 1
            else:
                l += 1
        return pairs
