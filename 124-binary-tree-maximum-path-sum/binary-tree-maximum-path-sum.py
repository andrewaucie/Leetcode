# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = float('-inf')
        def maxPathTraverse(root):
            nonlocal maxPath
            if not root:
                return 0
            left = maxPathTraverse(root.left)
            right = maxPathTraverse(root.right)
            bothPath = left + right + root.val
            singlePath = max(left, right, 0) + root.val
            maxPath = max(maxPath, singlePath, bothPath)
            return singlePath
        maxPathTraverse(root)
        return maxPath
