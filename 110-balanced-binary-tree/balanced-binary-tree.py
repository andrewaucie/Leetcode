# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def balanced(node):
            if not node:
                return [True, 0]
            leftBalanced, leftDepth = balanced(node.left)
            if not leftBalanced:
                return [False, 0]
            rightBalanced, rightDepth = balanced(node.right)
            if not rightBalanced:
                return [False, 0]
            return [abs(leftDepth-rightDepth) <= 1, max(leftDepth, rightDepth) + 1]
        return balanced(root)[0]