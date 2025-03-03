class Solution:
    """Sets entire rows and columns to zero if a zero is present in the matrix."""

    # Analysis: time = O(mn), space = O(1)
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """Modifies the matrix in-place by marking and setting rows and columns to zero."""
        if not matrix:
            return

        rows, cols = len(matrix), len(matrix[0])
        first_row_zeros = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zeros = any(matrix[i][0] == 0 for i in range(rows))

        # Mark rows & columns that should be zeroed
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero out columns
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(cols):
                    matrix[i][j] = 0

        # Zero out rows
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(rows):
                    matrix[i][j] = 0

        # Zero out the first row if needed
        if first_row_zeros:
            for j in range(cols):
                matrix[0][j] = 0

        # Zero out the first column if needed
        if first_col_zeros:
            for i in range(rows):
                matrix[i][0] = 0


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (
            [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
            [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
        ),
        (
            [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
            [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
        ),
        (
            [[1, 2, 3, 4, 5], [1, 2, 3, 0, 5], [1, 0, 3, 4, 5]],
            [[1, 0, 3, 0, 5], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
        ),
        (
            [[1, 2, 3], [4, 0, 6], [7, 8, 9]],
            [[1, 0, 3], [0, 0, 0], [7, 0, 9]],
        ),
    ]

    for i, (matrix, expected) in enumerate(test_cases, 1):
        solution.setZeroes(matrix)
        assert matrix == expected, f"Test case {i} failed"

    print("All test cases passed!")
