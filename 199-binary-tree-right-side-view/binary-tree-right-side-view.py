# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [(root, 0)]
        res = []
        levels = set()
        while stack:
            node, level = stack.pop()
            if level not in levels:
                res.append(node.val)
                levels.add(level)
            if node.left:
                stack.append((node.left, level+1))
            if node.right:
                stack.append((node.right, level+1))
        return res