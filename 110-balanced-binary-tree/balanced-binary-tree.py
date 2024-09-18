# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        balance = True
        def balanced(node):
            nonlocal balance
            if not node:
                return 0
            left = balanced(node.left)
            right = balanced(node.right)
            if abs(left - right) > 1:
                balance = False
            return max(left, right) + 1
        balanced(root)
        return balance