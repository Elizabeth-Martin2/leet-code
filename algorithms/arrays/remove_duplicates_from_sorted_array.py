class Solution:
    """Moves unique integers to the front and returns the count of unique numbers."""

    # Analysis: time = O(n), space = O(1)
    def remove_duplicates(self, nums: list[int]) -> int:
        if not nums:  # Base case
            return 0

        unique_ind = 1  # Slow pointer
        for fast in range(1, len(nums)):
            if nums[fast] != nums[unique_ind - 1]:
                nums[unique_ind] = nums[fast]
                unique_ind += 1

        return unique_ind


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ([2, 2, 2, 2, 2], 1, [2]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),  # Already unique
    ]

    for i, (nums, expected_len, expected_arr) in enumerate(test_cases, 1):
        result_len = solution.remove_duplicates(nums)
        assert result_len == expected_len, f"Test case {i} failed: expected {expected_len}, got {result_len}"
        assert nums[:result_len] == expected_arr, f"Test case {i} failed: expected array {expected_arr}, got {nums[:result_len]}"

    print("All test cases passed!")
