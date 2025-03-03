class Solution:
    """Returns the largest integer from an array."""

    # Analysis: O(n)
    def largest(self, arr: list[int]) -> int:
        return max(arr)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 8, 7, 56, 90], 90),
        ([10, 20, 30, 40, 50], 50),
        ([-10, -20, -30, -5], -5),
        ([100], 100),
    ]

    for i, (arr, expected) in enumerate(test_cases, 1):
        assert solution.largest(arr) == expected, f"Test case {i} failed"

    print("All test cases passed!")
