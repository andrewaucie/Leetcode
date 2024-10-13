# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        
        heap = []
        def perfectTree(root):
            if not root:
                return 0
            left = perfectTree(root.left) 
            right = perfectTree(root.right)
            if left == -1 or right == -1 or left != right:
                return -1

            heapq.heappush(heap, left + right + 1)
            if len(heap) > k:
                heapq.heappop(heap)

            return left + right + 1
        perfectTree(root)
        return heap[0] if len(heap) == k else -1