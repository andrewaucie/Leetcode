# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        depthDict = defaultdict(list)

        def traverse(node, depth):
            if not node:
                return
            depthDict[depth].append(node.val)
            traverse(node.left, depth+1)
            traverse(node.right, depth+1)
        
        traverse(root, 0)
        res = [[] for _ in range(len(depthDict))]
        for i in range(len(depthDict)):
            res[i] = depthDict[i]
        return res