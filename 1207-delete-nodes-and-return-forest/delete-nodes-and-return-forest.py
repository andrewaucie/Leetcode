# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        # def traverse(node, delete):
        #      if children in deleted set:
        #           recurse on traverse(child, True)
        #           node.left/right child = None
        #      else recurse on traverse(child, False)
        #      if delete = True:
        #           add children to root set
        #           
        #      
        #      
        # recurse on children, mark as deleted node
        #    [1]
        # [2]   [3]
        #[4][5] [6][7]
        if not root:
            return []

        to_delete = set(to_delete)
        rootSet = set()
        
        def dfs(node, isDelete):
            if node.left:
                if node.left.val in to_delete:
                    dfs(node.left, True)
                    node.left = None
                else:
                    dfs(node.left, False)
            if node.right:
                if node.right.val in to_delete:
                    dfs(node.right, True)
                    node.right = None
                else:
                    dfs(node.right, False)
            if isDelete:
                rootSet.update({node.left, node.right})
        
        deleteRoot = root.val in to_delete
        if not deleteRoot:
            rootSet.add(root)
        dfs(root, deleteRoot)
        return list(rootSet - {None})