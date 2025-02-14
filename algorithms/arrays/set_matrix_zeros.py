class Solution:
    """Sets the rows and columns of the matrix to zero if a zero is present in that row and column"""

    # Analysis: time = O(mn), space = O(1)
    def setZeroes(self, matrix: list[list[int]]) -> None:
        if not matrix:
            return

        # num rows = m ; num cols = n
        rows, cols = len(matrix), len(matrix[0])

        # Capture first row & col zeros first before overwriting
        first_row_zeros = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zeros = any(matrix[i][0] == 0 for i in range(rows))

        # Mark rows & columns with zeros
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

        # Finish with first rows
        if first_row_zeros:
            for j in range(cols):
                matrix[0][j] = 0
        if first_col_zeros:
            for i in range(rows):
                matrix[i][0] = 0

if __name__ == "__main__":
    solution = Solution()

    matrix1 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    solution.setZeroes(matrix1)
    assert matrix1 == [[0,0,0,0],[0,4,5,0],[0,3,1,0]], "Test case 1 failed"

    matrix2 = [[1,1,1],[1,0,1],[1,1,1]]
    solution.setZeroes(matrix2)
    assert matrix2 == [[1,0,1],[0,0,0],[1,0,1]], "Test case 2 failed"

    matrix3 = [[1,2,3,4,5],[1,2,3,0,5],[1,0,3,4,5]]
    solution.setZeroes(matrix3)
    assert matrix3 == [[1,0,3,0,5],[0,0,0,0,0],[0,0,0,0,0]], "Test case 3 failed"

    print("All test cases passed!")
