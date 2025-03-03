class Solution:
    """Finds the second largest integer in an array."""

    # Analysis: time = O(n), space = O(1)
    def get_second_largest(self, arr: list[int]) -> int:
        """Returns the second largest integer in the array, or -1 if it doesn't exist."""
        largest = second_largest = -1

        for num in arr:  # O(n)
            if num > largest:
                second_largest, largest = largest, num
            elif num > second_largest and num != largest:
                second_largest = num

        return second_largest


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([12, 35, 1, 10, 34, 1], 34),
        ([10, 5, 10], 5),
        ([10, 10, 10], -1),  # No second largest number
        ([3], -1),  # Single-element array
    ]

    for i, (arr, expected) in enumerate(test_cases, 1):
        assert solution.get_second_largest(arr) == expected, f"Test case {i} failed"

    print("All test cases passed!")
