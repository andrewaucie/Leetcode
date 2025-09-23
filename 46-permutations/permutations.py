class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(arr, i):
            if i == len(arr):
                res.append(arr[:])
            for j in range(i, len(arr)):
                arr[i], arr[j] = arr[j], arr[i]
                backtrack(arr, i+1)
                arr[i], arr[j] = arr[j], arr[i]
        backtrack(nums, 0)
        return res