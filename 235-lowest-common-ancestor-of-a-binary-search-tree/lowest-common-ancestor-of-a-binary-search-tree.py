# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        LCA = None
        maxDepth = 0
        def traverse(node, depth):
            nonlocal maxDepth, LCA
            if self.hasNode(node, p) and self.hasNode(node, q):
                if depth >= maxDepth:
                    maxDepth = depth
                    LCA = node
                traverse(node.left, depth+1)
                traverse(node.right, depth+1)
        traverse(root, 0)
        return LCA
            
    def hasNode(self, node, target):
        if not node:
            return False
        if node.val == target.val:
            return True
        return self.hasNode(node.left, target) or self.hasNode(node.right, target)
        