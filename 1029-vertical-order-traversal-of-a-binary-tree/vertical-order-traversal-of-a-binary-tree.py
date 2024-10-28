# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        positions = defaultdict(list)

        def dfs(node, col, row):
            positions[col].append((row, node.val))
            if node.left:
                dfs(node.left, col-1, row+1)
            if node.right:
                dfs(node.right, col+1, row+1)
        dfs(root, 0, 0)
        traversal = []
        for pos in sorted(positions.keys()):
            positions[pos].sort()
            traversal.append([val for _, val in positions[pos]])
        return traversal