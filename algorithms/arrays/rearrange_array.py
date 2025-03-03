class Solution:
    """Rearranges an array of positive and negative integers alternately."""

    # Analysis: time = O(n), space = O(n)
    # Note: A space O(1) solution exists but increases time complexity to O(n^2)
    def rearrange_array(self, nums: list[int]) -> list[int]:
        """
        Returns a list where:
        1. Consecutive numbers have opposite signs.
        2. Relative order of same-signed numbers is preserved.
        3. The first number is positive.
        """
        pos_nums, neg_nums = [], []
        for num in nums:
            if num > 0:
                pos_nums.append(num)
            else:
                neg_nums.append(num)
        
        return [x for pair in zip(pos_nums, neg_nums) for x in pair]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([3, 1, -2, -5, 2, -4], [3, -2, 1, -5, 2, -4]),
        ([-1, 1], [1, -1]),
        ([-2, -6, 3, 4, -5, 7], [3, -2, 4, -6, 7, -5]),
        ([5, -3, -2, 6, -1, 4], [5, -3, 6, -2, 4, -1]),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        assert solution.rearrange_array(nums) == expected, f"Test case {i} failed"

    print("All test cases passed!")
