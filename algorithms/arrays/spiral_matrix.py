class Solution:
    """Returns elements of a matrix in spiral order."""

    # Analysis: time = O(mn), space = O(1)
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        """Traverses the matrix in a clockwise spiral order."""
        res = []
        n_rows, n_cols = len(matrix), len(matrix[0])
        top_row, bottom_row = 0, n_rows - 1
        left_col, right_col = 0, n_cols - 1

        while top_row <= bottom_row and left_col <= right_col:
            # Go right
            for ind in range(left_col, right_col + 1):
                res.append(matrix[top_row][ind])
            top_row += 1 

            # Go down
            for ind in range(top_row, bottom_row + 1):
                res.append(matrix[ind][right_col])
            right_col -= 1 

            # Go left
            if top_row <= bottom_row:
                for ind in range(right_col, left_col - 1, -1):
                    res.append(matrix[bottom_row][ind])
                bottom_row -= 1

            # Go up
            if left_col <= right_col:
                for ind in range(bottom_row, top_row - 1, -1):
                    res.append(matrix[ind][left_col])
                left_col += 1

        return res


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
        ),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        ),
        ([[1]], [1]),
        ([[1, 2], [3, 4]], [1, 2, 4, 3]),
        ([[1, 2, 3]], [1, 2, 3]),
        ([[1], [2], [3]], [1, 2, 3]),
    ]

    for i, (matrix, expected) in enumerate(test_cases, 1):
        assert solution.spiralOrder(matrix) == expected, f"Test case {i} failed"

    print("All test cases passed!")
