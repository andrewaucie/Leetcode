# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if bool(root1) != bool(root2):
            return False
        if root1 and root2 and (root1.val != root2.val):
            return False
        queue = deque()
        if root1:
            queue.append((root1, 1))
        if root2:
            queue.append((root2, -1))
        while queue:
            nodeCount = defaultdict(lambda: defaultdict(int))
            for _ in range(len(queue)):
                parent, treeDelta = queue.popleft()
                for child in (parent.left, parent.right):
                    if child:
                        nodeCount[parent.val][child.val] += treeDelta
                        if nodeCount[parent.val][child.val] == 0:
                            del nodeCount[parent.val][child.val]
                            if not nodeCount[parent.val]:
                                del nodeCount[parent.val]
                        queue.append((child, treeDelta))
            if nodeCount:
                return False
        return True

#   0
#  3 1
#     2

#   0
#  3 1
# 2    