class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n_rows = len(matrix)
        n_cols = len(matrix[0])

        # first transpose matrix
        for row in range(n_rows):
            for col in range(row + 1, n_cols):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        # now reverse rows
        for row in range(n_rows):
            matrix[row].reverse()
       
if __name__ == "__main__":
    solution = Solution()

    matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
    sol1 = [[7,4,1],[8,5,2],[9,6,3]]
    solution.rotate(matrix1)

    for i in range(len(matrix1)):
        assert matrix1[i] == sol1[i]

    matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    sol2 = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    solution.rotate(matrix2)

    for i in range(len(matrix2)):
        assert matrix2[i] == sol2[i]

    print("All test cases passed!")