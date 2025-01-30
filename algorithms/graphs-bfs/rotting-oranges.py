class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        total_rows, total_cols = len(grid), len(grid[0])

        rotten_oranges = deque()
        fresh_oranges = 0

        # Find all rotten & fresh oranges
        for row in range(0, total_rows):
            for column in range(0, total_cols):
                if grid[row][column] == 1:
                    # print(f"Found fresh orange at: {row, column}")
                    fresh_oranges += 1
                
                if grid[row][column] == 2:
                    # print(f"Found rotten orange at: {row, column}")
                    rotten_oranges.append((row, column))

        # Base cases
        if fresh_oranges == 0:  # Either entirely empty or only rotten oranges
            return fresh_oranges
        if len(rotten_oranges) == 0:  # Full of fresh oranges that will magically never rot
            return -1

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right
        
        mins = 0
        while rotten_oranges and fresh_oranges > 0:
            for _ in range(len(rotten_oranges)):
                row, col = rotten_oranges.popleft()
                for dir_row, dir_col in dirs:
                    new_row, new_col = row + dir_row, col + dir_col # Takes a step in a direction
                    if 0 <= new_row < total_rows and 0 <= new_col < total_cols and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2 # Mark as rotten
                        fresh_oranges -= 1
                        rotten_oranges.append((new_row, new_col))
            mins += 1
        
        return mins if fresh_oranges == 0 else -1