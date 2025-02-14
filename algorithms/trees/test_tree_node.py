import unittest
from tree_node import TreeNode


class TestTreeNode(unittest.TestCase):

    def test_create_tree(self):
        test_tree_structure = [1, 2, 3, None, 4, 5, 6]
        test_tree = TreeNode.create_tree(test_tree_structure)

        self.assertEqual(test_tree.val, 1)
        self.assertEqual(test_tree.left.val, 2)
        self.assertEqual(test_tree.right.val, 3)
        self.assertIsNone(test_tree.left.left)
        self.assertEqual(test_tree.left.right.val, 4)
        self.assertEqual(test_tree.right.left.val, 5)
        self.assertEqual(test_tree.right.right.val, 6)

    def test_empty_tree(self):
        test_tree = TreeNode.create_tree([])
        self.assertIsNone(test_tree)

    def test_single_node_tree(self):
        test_tree = TreeNode.create_tree([1])
        self.assertEqual(test_tree.val, 1)
        self.assertIsNone(test_tree.left)
        self.assertIsNone(test_tree.right)


if __name__ == "__main__":
    unittest.main()
