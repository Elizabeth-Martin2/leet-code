class Solution:
    """
    Given a 2D array (mat) where no two adjacent cells are equal, return
    a (any) peak element coordinate.

    Uses binary search to find the peak elements.

    LC. 1901 Find a Peak Element 2
    """

    # Helper function anaysis
    # time = O(n), space = O(1)
    # where n = number of rows
    def maxRow(self, mat: list[list[int]], col_ind) -> list[int]:
        max_val, ind = float('-inf'), 0
        
        for num in range(0, len(mat)):
            if mat[num][col_ind] > max_val:
                max_val = mat[num][col_ind]
                ind = num
        
        return [max_val, ind]


    # Overall analysis (including helper function)
    # time = O(n * log(m)), space = O(1)
    # where m = number of columns, n = number of rows
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        num_rows, num_cols = len(mat), len(mat[0])
        
        left, right = 0, num_cols - 1
        while left <= right:
            mid = (left + right) // 2
            
            max_val, ind = self.maxRow(mat, mid)
            left_neighbor = mat[ind][mid - 1] if mid > 0 else -1
            right_neighbor = mat[ind][mid + 1] if mid < num_cols -1 else -1
            
            if left_neighbor < max_val > right_neighbor:
                return [ind, mid]
            elif right_neighbor > max_val:
                left = mid + 1
            else:
                right = mid - 1
            
        # Shouldn't reach here, included for completion
        return [-1, -1]

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([[1,4],[3,2]], [[0,1], [1,0]]),
        ([[10,20,15],[21,30,14],[7,16,32]], [[1,1], [2,2]]),
        ([[1,2,6],[3,4,5]], [[0,2]])
    ]

    for i, (matrix, peaks) in enumerate(test_cases, 1):
        output = solution.findPeakGrid(matrix)
        assert output in peaks, f"Test case {i} failed, expected one of {peaks}, got {output}"

    print("All test cases passed!")