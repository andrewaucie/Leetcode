class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.data = data
        self.tree = [0] * (self.n * 2)

        for i in range(1, self.n - 1):
            left = self.data[i-1]
            right = self.data[i+1]
            # 1 if peak, 0 otherwise
            self.tree[i + self.n] = int(self.data[i] > left and self.data[i] > right)

        for i in range(self.n-1, 0, -1):
            leftChild = self.tree[i*2]
            rightChild = self.tree[i*2 + 1]
            self.tree[i] = leftChild + rightChild
    
    def update(self, pos, val):
        self.data[pos] = val

        for i in range(pos-1, pos+2):
            if not (0 < i < self.n-1):
                continue
            
            left = self.data[i-1]
            right = self.data[i+1]
            newPos = i + self.n
            # update peak -> no peak, or no peak -> peak
            if self.data[i] > left and self.data[i] > right:
                if self.tree[newPos] == 0:
                    self.tree[newPos] = 1
                    while newPos > 1:
                        newPos //= 2
                        self.tree[newPos] = self.tree[newPos * 2] + self.tree[newPos * 2 + 1]
            else:               
                if self.tree[newPos] == 1:
                    self.tree[newPos] = 0
                    while newPos > 1:
                        newPos //= 2
                        self.tree[newPos] = self.tree[newPos * 2] + self.tree[newPos * 2 + 1]
                
    def query(self, l, r):
        l += self.n
        r += self.n + 1
        res = 0
        while l < r:
            if l%2 == 1:
                res += self.tree[l]
                l += 1
            if r%2 == 1:
                r -= 1
                res += self.tree[r]
            l //= 2
            r //= 2
        return res       

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        root = SegmentTree(nums)
        res = []
        for typ, param1, param2 in queries:
            if typ == 1:
                res.append(root.query(param1+1, param2-1))
            else:
                root.update(param1, param2)
        return res