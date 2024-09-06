# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def bst(node, depth):
            if not node:
                return depth
            return max(bst(node.left, depth+1), bst(node.right, depth+1))
        return bst(root,0)