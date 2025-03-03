class Solution:
    """Rotates an n x n matrix 90 degrees clockwise in-place."""

    # Analysis: time = O(n^2), space = O(1)
    def rotate(self, matrix: list[list[int]]) -> None:
        """Modifies the matrix in-place by first transposing and then reversing each row."""
        n = len(matrix)

        # Transpose the matrix
        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        # Reverse each row
        for row in matrix:
            row.reverse()


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[7, 4, 1], [8, 5, 2], [9, 6, 3]],
        ),
        (
            [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
            [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
        ),
    ]

    for i, (matrix, expected) in enumerate(test_cases, 1):
        solution.rotate(matrix)
        assert matrix == expected, f"Test case {i} failed"

    print("All test cases passed!")
