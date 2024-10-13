# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        
        res = []
        def perfectTree(root):
            if not root:
                return 0
            left = perfectTree(root.left) 
            right = perfectTree(root.right)
            if left == -1 or right == -1 or left != right:
                return -1

            res.append(left + right + 1)

            return left + right + 1
        perfectTree(root)
        res.sort(reverse=True)
        if len(res) >= k:
            return res[k-1]
        return -1
