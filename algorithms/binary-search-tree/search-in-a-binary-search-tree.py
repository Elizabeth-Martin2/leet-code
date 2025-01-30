# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        expl = root
        # Base cases
        if expl is None:
            return expl
        if expl.val == val:
            return expl
        
        if val <= root.val:
            return self.searchBST(expl.left, val)
        else:
            return self.searchBST(expl.right, val)