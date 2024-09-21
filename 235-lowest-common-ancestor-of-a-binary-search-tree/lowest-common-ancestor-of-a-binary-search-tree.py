# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pathP = self.createPath(root, p, [root])
        pathQ = self.createPath(root, q, [root])
        i = 0
        while i < len(pathP)-1 and i < len(pathQ)-1 and pathP[i+1] == pathQ[i+1]:
            i += 1
        return pathP[i]
            
    def createPath(self, node, target, path):
        if not node:
            return [None]
        if node.val == target.val:
            return path + [target]
        left = self.createPath(node.left, target, path + [node.left])
        right = self.createPath(node.right, target, path + [node.right])
        if left[-1] == target:
            return left
        elif right[-1] == target:
            return right
        return [None]