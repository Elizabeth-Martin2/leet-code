class Solution:
    """
    Given a grid of values 0, 1, 2, determine the minimum number of
    operations required to change cell values such that all cells
    that belong to the shape of a 'Y' have the same value, and all
    other cells have a different (but uniform) value.

    LC. 3071 Minimum Operations to Write the Letter Y on a Grid
    """

    # Function Analysis: time = O(n), space = O(1)
    def buildYCells(self, n: int) -> set[tuple[int, int]]:
        y_cells = set()
        mid = n // 2

        # on upper left arm of Y
        for i in range(mid + 1):
            y_cells.add((i, i))

        # on upper right arm of Y
        i, j = 0, n - 1
        while i < j:
            y_cells.add((i, j))
            i += 1
            j -= 1

        # on bottom of Y
        for i in range(mid, n):
            y_cells.add((i, mid))

        return y_cells


    # Overall Analysis: time = O(n^2), space = O(1)
    def minimumOperationsToWriteY(self, grid: list[list[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        
        y_count, y_freq = 0, {0:0, 1:0, 2:0}
        o_count, o_freq = 0, {0:0, 1:0, 2:0}

        y_cells = self.buildYCells(num_rows)

        for row in range(num_rows):
            for col in range(num_cols):
                if (row, col) in y_cells:
                    y_count += 1
                    y_freq[grid[row][col]] += 1
                else:
                    o_count += 1
                    o_freq[grid[row][col]] += 1
        
        min_ops = float('inf')

        for y_digit in range(3):
            for o_digit in range(3):
                if y_digit == o_digit:
                    continue

                ops_y = y_count - y_freq[y_digit]
                ops_o = o_count - o_freq[o_digit]
                min_ops = min(min_ops, ops_y + ops_o)

        return min_ops
    

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([[1,2,2],[1,1,0],[0,1,0]], 3),
        ([[0,1,0,1,0],[2,1,0,1,2],[2,2,2,0,1],[2,2,2,2,2],[2,1,2,2,2]], 12),
        ([[0,0,1],[0,0,2],[1,0,2]], 4)
    ]

    for i, (grid, expected) in enumerate(test_cases, 1):
        output = solution.minimumOperationsToWriteY(grid)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")