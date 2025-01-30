class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_coords = []
        row_count = len(matrix)
        col_count = len(matrix[0])
        for m, row in enumerate(matrix):
            for n, col in enumerate(row):
                if col == 0:
                    zero_coords.append((m,n))
                    

        # print(zero_coords)
        # print(f"row count: {row_count} ; col count: {col_count}")
        for entry in zero_coords:
            # Set row to 0s
            for current_row in range(0, row_count):
                # print(f"Row: setting {[entry[0]]}{[current_row]} entry to 0")
                matrix[current_row][entry[1]] = 0
            # Set col to 0s
            for current_col in range(0, col_count):
                # print(f"Col: setting {[current_col]}{[entry[1]]} entry to 0")
                matrix[entry[0]][current_col] = 0
