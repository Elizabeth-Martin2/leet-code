# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leaf_generator(self, root: Optional[TreeNode]):
        if root:
            if not root.left and not root.right:
                yield root.val  # Yield the leaf node value
            else:
                yield from self.leaf_generator(root.left)  # Traverse left subtree
                yield from self.leaf_generator(root.right)  # Traverse right subtree

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Convert generator outputs to lists and compare them
        return list(self.leaf_generator(root1)) == list(self.leaf_generator(root2))