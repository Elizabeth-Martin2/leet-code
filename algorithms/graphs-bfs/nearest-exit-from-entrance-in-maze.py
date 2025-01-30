class Solution:
    def isExit(current: List[int], total_rows: int, total_cols: int, entrance: List[int]) -> bool:
        if current != entrance:
            # Top or bottom
            if current[0] == 0 or current[0] == total_rows:
                return True
            # Left or right
            elif current[1] == 0 or current[1] == total_cols:
                return True
        
        return False


    def isSafeStep(target: List[int], total_rows:int, total_cols: int, maze: List[List[str]]) -> bool:
        tar_row = target[0]
        tar_col = target[1]
        # Inside maze rows
        if tar_row >= 0 and tar_row <= total_rows: 
            # Inside maze columns
            if tar_col >= 0 and tar_col <= total_cols:
                # Not a wall
                if maze[target[0]][target[1]] != "+":
                    return True
        
        return False

   
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        total_cols = len(maze[0]) - 1
        total_rows = len(maze) - 1

        visited = set()
        visited.add((entrance[0], entrance[1]))
        steps = 0
        q = deque([entrance])

        while q:
            for _ in range(len(q)):
                current = q.popleft() 
                row = current[0]
                column = current[1]
                
                if Solution.isExit(current, total_rows, total_cols, entrance):
                    return steps
                
                # look above
                step_above = [(row - 1), column]
                if Solution.isSafeStep(step_above, total_rows, total_cols, maze) and (step_above[0], step_above[1]) not in visited:
                    visited.add((step_above[0], step_above[1]))
                    q.append(step_above)
                    
                # look below
                step_below = [(row + 1), column]
                if Solution.isSafeStep(step_below, total_rows, total_cols, maze) and (step_below[0], step_below[1]) not in visited:
                    visited.add((step_below[0], step_below[1]))
                    q.append(step_below)
                
                # look left
                step_left = [row, (column - 1)]
                if Solution.isSafeStep(step_left, total_rows, total_cols, maze) and (step_left[0], step_left[1]) not in visited:
                    visited.add((step_left[0], step_left[1]))
                    q.append(step_left)

                # look right
                step_right = [row, (column + 1)]
                if Solution.isSafeStep(step_right, total_rows, total_cols, maze) and (step_right[0], step_right[1]) not in visited:
                    visited.add((step_right[0], step_right[1]))
                    q.append(step_right)

            steps += 1

        return -1



