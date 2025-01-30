class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []  
        if not root:
            return res
        
        queue = deque([root]) 

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()  

                # Only append if it's the node on the right
                if i == level_size - 1: 
                    res.append(node.val)
                    
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return res