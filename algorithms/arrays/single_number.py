class Solution:
    """Finds the single non-duplicate number in an array using XOR."""

    # Analysis: time = O(n), space = O(1)
    def single_number(self, nums: list[int]) -> int:
        """Returns the single number in a given array where every other number appears twice."""
        result = 0
        for num in nums:
            result ^= num
        return result


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([4, 1, 2, 1, 2], 4),
        ([2, 2, 1], 1),
        ([1], 1),
        ([0, 1, 0], 1),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        assert solution.single_number(nums) == expected, f"Test case {i} failed"

    print("All test cases passed!")
