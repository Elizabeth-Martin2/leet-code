class Solution:
    """Finds the maximum subarray sum using Kadane's Algorithm."""

    DEBUG = False
    @staticmethod
    def _debug(*args, **kwargs):
        if Solution.DEBUG:
            print(*args, **kwargs)

    # Analysis: time = O(n), space = O(1)
    def max_sub_array(self, nums: list[int]) -> int:
        """Returns the sum of the maximum subarray."""
        current_sum = max_sum = nums[0]
        
        for num in nums[1:]:
            Solution._debug(f"current_sum: {current_sum}, max_sum: {max_sum}, num: {num}")
            current_sum = max(current_sum + num, num)
            max_sum = max(current_sum, max_sum)

        return max_sum


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
        ([-1, -2, -3, -4], -1),  # Edge case: all negative numbers
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        assert solution.max_sub_array(nums) == expected, f"Test case {i} failed"

    print("All test cases passed!")
