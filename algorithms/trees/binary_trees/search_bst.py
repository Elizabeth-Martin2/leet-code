from typing import Optional
from algorithms.trees.tree_node import TreeNode

class Solution:
    def search_bst(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Searches for a given value in a Binary Search Tree (BST).
        """
        if root is None or root.val == val:
            return root

        if val <= root.val:
            return self.search_bst(root.left, val)
        else:
            return self.search_bst(root.right, val)

if __name__ == "__main__":
    tree = TreeNode.create_tree([4, 2, 7, 1, 3])
    sol = Solution()

    result = sol.search_bst(tree, 2)
    assert result is not None and result.val == 2, "Test failed: Expected node with value 2"

    result = sol.search_bst(tree, 5)
    assert result is None, "Test failed: Expected None for value 5"

    result = sol.search_bst(None, 3)
    assert result is None, "Test failed: Expected None for empty tree"

    print("All test cases passed!")