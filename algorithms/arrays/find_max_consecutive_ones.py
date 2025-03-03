class Solution:
    """Finds the maximum number of consecutive ones"""

    # Analysis: time = O(n), space = O(1)
    def find_max_consecutive_ones(self, nums: list[int]) -> int:
        """Returns the maximum number of consecutive ones in a binary array"""
        max_count = current_count = 0
        for num in nums:
            if num == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
        return max_count


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1, 1, 0, 1, 1, 1], 3),
        ([1, 0, 1, 1, 0, 1], 2),
        ([0, 0, 0, 0], 0),
        ([1, 1, 1, 1, 1], 5),
    ]

    for nums, expected in test_cases:
        assert solution.find_max_consecutive_ones(nums) == expected

    print("All test cases passed!")
