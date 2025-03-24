class Solution:
    """
    Return the row index in a given 2D array (arr) with
    the maximum number of ones.

    Uses binary search to find the row.
    """

    # Analysis: time = O(n log m), space = O(1)
    # where n = number of rows and m = number of columns
    def rowWithMax1s(self, arr: list[int]) -> int:
        num_cols = len(arr[0])
        left, right = 0, num_cols
        target_row = -1
        
        while left < right:
            mid = (left + right) // 2
            
            found_ones = False
            for i, row in enumerate(arr):
                if row[mid] == 1:
                    found_ones = True
                    target_row = i
                    break
            
            if found_ones:
                right = mid
            else:
                left = mid + 1
                
        return target_row


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]], 2),
        ([[0,0], [1,1]], 1),
        ([[0,0], [0,0]], -1)
    ]

    for i, (arr, expected) in enumerate(test_cases, 1):
        output = solution.rowWithMax1s(arr)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")