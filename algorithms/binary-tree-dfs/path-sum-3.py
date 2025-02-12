from collections import defaultdict # Fills prefix_sums with zeros for cleaner code

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def solve(self, node, curr_sum: int, targetSum: int, prefix_sums: dict) -> int:
        if node is None:
            return 0
        
        curr_sum += node.val 
        count = prefix_sums[curr_sum - targetSum]

        prefix_sums[curr_sum] += 1

        count += self.solve(node.left, curr_sum, targetSum, prefix_sums)
        count += self.solve(node.right, curr_sum, targetSum, prefix_sums)

        # Remove the current prefix sum before returning (backtracking)
        prefix_sums[curr_sum] -= 1  
        return count
	
    def path_sum(self, root: TreeNode, targetSum: int) -> int:
        if root is None:
            return 0
        
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1 # Base case: if target sum is found when starting from root

        return self.solve(root, 0, targetSum, prefix_sums)
