from collections import deque
class Solution:
    """
    Given a grid of 1's and 0's (grid) representing land and water (respectively),
    return the number of islands.

    LC. 200 Number of Islands
    """

    def floodFill(self, grid: list[list[str]], sr: int, sc: int) -> None:
        num_rows, num_cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        to_visit = deque()
        to_visit.append([sr,sc])

        while to_visit:
            current_row, current_col = to_visit.popleft()
            grid[current_row][current_col] = '0'

            for delta_row, delta_col in directions:
                next_row, next_col = current_row + delta_row, current_col + delta_col

                if 0 <= next_row < num_rows and 0 <= next_col < num_cols and grid[next_row][next_col] == '1':
                    to_visit.append([next_row, next_col])
                    grid[next_row][next_col] = '0'


    def numIslands(self, grid: list[list[str]]) -> int:
        islands = 0
        
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col] == '1':
                    self.floodFill(grid, row, col)
                    islands += 1
        
        return islands


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]], 1),
        ([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]], 3),
        ([["1"]], 1),
        ([["0"]], 0)
    ]

    for i, (grid, expected) in enumerate(test_cases, 1):
        output = solution.numIslands(grid)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")