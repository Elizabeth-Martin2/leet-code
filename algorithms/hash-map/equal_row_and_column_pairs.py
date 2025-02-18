class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        grid_len = len(grid)
        duplicates = 0
        row_counts = {}
        for row in grid:
            if tuple(row) not in row_counts:
                row_counts[tuple(row)] = 0
            row_counts[tuple(row)] +=1
                    
        # print(row_counts)
        transpose_matrix = [[] for _ in range(grid_len)]
        # Take transpose of grid
        for row in grid:
            for i in range(grid_len):
                transpose_matrix[i].append(row[i])
        # print(transpose_matrix)
        
        for row in transpose_matrix:
            if tuple(row) in row_counts:
                duplicates += row_counts[tuple(row)]

        # print(duplicates)
        return duplicates


# Complexity: O(n^2)
    # Row 6: n rows x converting n elements to a tuple = O(n^2)
    # Row 14: n rows x n cols = O(n^2)
    # Row 19: n rows x converting n elements to a tule = O(n^2)