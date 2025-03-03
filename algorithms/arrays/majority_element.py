import math

class Solution:
    """Finds the majority element in an array."""

    # Analysis: time = O(n), space = O(1)
    def majority_element_half(self, nums: list[int]) -> int:
        """Returns the element appearing more than half the time using Boyer-Moore Voting."""
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate

    # Analysis: time = O(n), space = O(1)
    def majority_element_third(self, nums: list[int]) -> list[int]:
        """Returns elements appearing more than a third of the time using Boyer-Moore Voting."""
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        res = []
        maj = math.floor(len(nums) / 3)
        if count1 > maj:
            res.append(candidate1)
        if count2 > maj:
            res.append(candidate2)

        return res


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([3, 2, 3], 3, [3]),
        ([2, 2, 1, 1, 1, 2, 2], 2, [2, 1]),
        ([1], 1, [1]),
        ([1, 2], None, [1, 2]),
    ]

    for i, (nums, expected_half, expected_third) in enumerate(test_cases, 1):
        if expected_half is not None:
            assert solution.majority_element_half(nums) == expected_half, f"Test case {i} (half) failed"
        assert solution.majority_element_third(nums) == expected_third, f"Test case {i} (third) failed"

    print("All test cases passed!")
