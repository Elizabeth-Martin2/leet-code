class Solution:
    """
    Returns the floor and ceiling integers for a given target in a sorted array.
    Uses binary search to find the floor & ceiling.
    """

    # Analysis: time = O(log n), space = O(1)
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        # arr.sort()
        left, right = 0, len(arr) - 1
        floor, ceil = -1, -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == x:
                return x, x

            elif arr[mid] < x:
                floor = arr[mid]
                left = mid + 1
            
            else: # arr[mid] > x
                ceil = arr[mid]
                right = mid - 1
        
        return floor, ceil


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([17, 21, 36, 56, 73, 82, 86, 88], 17, 17, 17),
        ([1, 3, 5, 6, 6, 7, 8, 12], 9, 8, 12),
        ([1, 2, 8, 10, 10, 12, 19], 5, 2, 8)
    ]

    for i, (test, target, floor, ceiling) in enumerate(test_cases):
        output_floor, output_ceiling = solution.getFloorAndCeil(target, test)
        assert output_floor == floor, f"Test case {i + 1} floor failed, expected {floor}, got {output_floor}"
        assert output_ceiling == ceiling, f"Test case {i + 1} ceiling failed, expected {ceiling}, got {output_ceiling}"

    print("All test cases passed!")