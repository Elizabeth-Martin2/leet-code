class Solution:
    """Checks if an increasing triplet subsequence exists in the list."""

    def increasingTriplet(self, nums: list[int]) -> bool:
        # Base case
        length = len(nums)
        if length < 3:
            return False

        small = med = float('inf')
        for num in nums:
            if num < small:
                small = num
            elif small < num < med:
                med = num
            elif num > med:
                return True

        return False


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 2, 3, 4, 5], True),
        ([5, 4, 3, 2, 1], False),
        ([2, 1, 5, 0, 4, 6], True),
        ([20, 100, 10, 12, 5, 13], True),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        assert solution.increasingTriplet(nums) == expected, f"Test case {i} failed"

    print("All test cases passed!")
