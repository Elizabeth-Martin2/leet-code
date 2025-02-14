# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # branchMax = current max value in branch
    # numGoodNodes = number of good nodes
    @staticmethod
    def dfsRec(root: TreeNode, branchMax:int) -> int:
        # Stopping condition / base case
        if root is None:
            return 0
        
        numGoodNodes = 1 if root.val >= branchMax else 0

        branchMax = max(root.val, branchMax)

        numGoodNodes += Solution.dfsRec(root.left, branchMax)
        numGoodNodes += Solution.dfsRec(root.right, branchMax)
        return numGoodNodes
        

    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        return Solution.dfsRec(root, root.val)