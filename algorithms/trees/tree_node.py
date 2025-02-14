from collections import deque
from typing import Optional


class TreeNode:
    """
    Represents a binary tree with a value, left child, and right child
    """

    def __init__(
        self,
        val: int = 0,
        left: "TreeNode" = None,
        right: "TreeNode" = None
    ):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def create_tree(
            tree_structure: list[Optional[int]]
            ) -> Optional["TreeNode"]:
        """
        Constructs a binary tree from a level-order list representation.
        """
        if not tree_structure:
            return None

        root = TreeNode(tree_structure[0])
        queue = deque([root])
        i = 1

        while i < len(tree_structure):
            node = queue.popleft()

            if i < len(tree_structure) and tree_structure[i] is not None:
                node.left = TreeNode(tree_structure[i])
                queue.append(node.left)
            i += 1

            if i < len(tree_structure) and tree_structure[i] is not None:
                node.right = TreeNode(tree_structure[i])
                queue.append(node.right)
            i += 1

        return root
