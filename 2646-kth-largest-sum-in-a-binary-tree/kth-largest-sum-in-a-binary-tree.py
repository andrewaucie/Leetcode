# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = defaultdict(int)
        def traverse(root, level):
            if not root:
                return
            sums[level] += root.val
            traverse(root.left, level+1)
            traverse(root.right, level+1)
        traverse(root, 0)
        if len(sums) < k:
            return -1
        return sorted(sums.values(), reverse=True)[k-1]