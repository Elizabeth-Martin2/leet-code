class Solution:
    """Computes the product of all elements except self in an array."""

    # Analysis: time = O(n), space = O(n)
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """Returns an array where each element is the product of all elements except itself."""
        n = len(nums)
        prefix_prods = [1] * n
        sol = [1] * n

        # Compute prefix products
        for i in range(1, n):
            prefix_prods[i] = prefix_prods[i - 1] * nums[i - 1]

        # Compute suffix products and final result
        suffix_prod = 1
        for i in range(n - 1, -1, -1):
            sol[i] = prefix_prods[i] * suffix_prod
            suffix_prod *= nums[i]

        return sol


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([0, 1, 2, 3], [6, 0, 0, 0]),
        ([4, 5, 1, 8], [40, 32, 160, 20]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        assert solution.productExceptSelf(nums) == expected, f"Test case {i} failed"

    print("All test cases passed!")
