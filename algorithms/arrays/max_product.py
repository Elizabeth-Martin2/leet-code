class Solution:
    """Returns the max product in the given array."""

    # Analysis: time = O(n), space = O(1)
    def maxProduct(self, nums: list[int]) -> int:
        res, max_prod, min_prod = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:
                max_prod, min_prod = min_prod, max_prod

            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)

            res = max(res, max_prod)

        return res


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([2,3,-2,4], 6),
        ([-2,0,-1], 0),
        ([-2,3,-4], 24)
    ]

    for i, (test, expected) in enumerate(test_cases):
        output = solution.maxProduct(test)
        assert output == expected, f"Test case {i + 1} failed, expected: {expected}, got: {output}"

    print("All test cases passed!")