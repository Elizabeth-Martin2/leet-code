class Solution:
    """
    Returns True if given target is present in a 2D matrix, else False.
    Uses binary search to find the target.

    Given: (1) Each row is sorted in non-decreasing order.  (2) The first
    integer of each row is greater than the last integer of the previous row.

    LC. 74 Search a 2D matrix
    """

    # Analysis: time = O(log(m*n)), space = O(1)
    # where m = number of columns, n = number of rows
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:        
        num_rows, num_cols = len(matrix), len(matrix[0])

        low, high = 0, (num_rows * num_cols) - 1

        while low <= high:
            mid = (low + high) // 2
            mid_val = matrix[mid // num_cols][mid % num_cols]

            if mid_val == target:
                return True

            elif mid_val > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return False

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3, True),
        ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13, False),
        ([[1]], 2, False)
    ]

    for i, (matrix, target, expected) in enumerate(test_cases, 1):
        output = solution.searchMatrix(matrix, target)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")