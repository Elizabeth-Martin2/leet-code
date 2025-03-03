class Solution:
    """Performs in-place array rotation."""

    def reverse(self, nums: list[int], left: int, right: int):
        """Reverses integers between left & right positions."""
        while left < right:  # O(right - left)
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    # Analysis: time = O(n), space = O(1)
    def rotate(self, nums: list[int], k: int) -> None:
        """Rotates an array k positions to the right in-place."""
        n = len(nums)
        if not nums or len(nums) == 1:
            return

        k %= n  # Handles cases where k > n
        self.reverse(nums, 0, n - 1)  # O(n)
        self.reverse(nums, 0, k - 1)  # O(k)
        self.reverse(nums, k, n - 1)  # O(n - k)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([1, 2], 3, [2, 1]),
        ([-1], 2, [-1]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
    ]

    for i, (nums, k, expected) in enumerate(test_cases, 1):
        solution.rotate(nums, k)
        assert nums == expected, f"Test case {i} failed"

    print("All test cases passed!")
