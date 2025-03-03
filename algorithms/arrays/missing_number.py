class Solution:
    """Finds the missing number in an array of n distinct numbers."""

    # Analysis: time = O(n), space = O(1)
    def missing_number(self, nums: list[int]) -> int:
        """Returns the missing number using Gauss' formula."""
        n = len(nums)
        expected_sum = n * (n + 1) // 2  # Gauss' formula for sum 0 to n
        actual_sum = sum(nums)
        return expected_sum - actual_sum


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        ([1], 0),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        assert solution.missing_number(nums) == expected, f"Test case {i} failed"

    print("All test cases passed!")
