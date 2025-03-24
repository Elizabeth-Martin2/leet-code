class Solution:
    """
    Returns True if given target is present in a 2D matrix, else False.

    Given: (1) Integers in each row are sorted in ascending from left to right.
    (2) Integers in each column are sorted in ascending from top to bottom.

    LC. 240 Search a 2D matrix 2
    """

    # Analysis: time = O(m + n), space = O(1)
    # where m = number of columns, n = number of rows
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        num_rows, num_cols = len(matrix), len(matrix[0])
        c_row, c_col = 0, num_cols - 1

        # Key insight: bottom left & top right are the best starting points
        # From top right, every value to the left is smaller and all values
        # below are larger
        while c_row < num_rows and c_col >= 0:
            c_val = matrix[c_row][c_col]

            if target == c_val:
                return True
            if target < c_val:
                c_col -= 1
            else:
                c_row += 1

        return False

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5, True),
        ([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20, False),
        ([[1]], 2, False)
    ]

    for i, (matrix, target, expected) in enumerate(test_cases, 1):
        output = solution.searchMatrix(matrix, target)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")