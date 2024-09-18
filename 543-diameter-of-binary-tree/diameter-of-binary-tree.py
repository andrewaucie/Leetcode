# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxPath = 0
        def longestPath(node):
            if not node:
                return 0
            nonlocal maxPath
            left = longestPath(node.left)
            right = longestPath(node.right)
            maxPath = max(maxPath, left + right)
            return max(left, right) + 1
        longestPath(root)
        return maxPath