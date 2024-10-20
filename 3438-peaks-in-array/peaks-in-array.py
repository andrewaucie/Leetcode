class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums
        self.tree = [0] * 2 * len(nums)
        for i in range(1, self.n-1):
            self.tree[i + self.n] = int(self.nums[i] > max(self.nums[i-1], self.nums[i+1]))
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.tree[i*2] + self.tree[i*2 + 1]
    
    def update(self, index, val):
        self.nums[index] = val

        for i in range(index-1, index+2):
            if not (0 < i < self.n-1):
                continue
            newPos = self.n + i
            if self.nums[i] > max(self.nums[i-1], self.nums[i+1]):
                if self.tree[newPos] == 0:
                    self.tree[newPos] = 1
                    while newPos > 1:
                        newPos //= 2
                        self.tree[newPos] = self.tree[newPos*2] + self.tree[newPos*2+1]
            else:
                if self.tree[newPos] == 1:
                    self.tree[newPos] = 0
                    while newPos > 1:
                        newPos //= 2
                        self.tree[newPos] = self.tree[newPos*2] + self.tree[newPos*2+1]

    def query(self, l, r):
        l += self.n
        r += self.n
        peaks = 0
        while l <= r:
            if l % 2 == 1:
                peaks += self.tree[l]
                l += 1
            if r % 2 == 0:
                peaks += self.tree[r]
                r -= 1
            l //= 2
            r //= 2
        return peaks
        
class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        tree = SegmentTree(nums)
        res = []
        for op, param1, param2 in queries:
            if op == 1:
                res.append(tree.query(param1+1, param2-1))
            else:
                tree.update(param1, param2)
        return res