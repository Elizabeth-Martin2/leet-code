class Solution:
    """
    Given an array of integers (nums) and an integer threshold (threshold), we will choose
    a positive integer divisor, divide all the array by it, and sum the division's result.
    Return the smallest divisor such that the result mentioned above is less than or equal
    to threshold.

    Uses binary search to find the divisor

    LC. 1283 Find the smallest Divisor Given a Threshold
    """

    # Analysis: time = O(n log m), space = O(1)
    # where m = max(nums) and n = len(nums)
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        left, right = 1, max(nums)

        while left < right:
            divisor = (left + right) // 2
            
            current_sum = 0
            for num in nums:
                res = (num + divisor - 1) // divisor # equivalent to ceil.
                current_sum += res
            
            if current_sum > threshold:
                left = divisor + 1
            else:
                right = divisor

        return left


if __name__ == "__main__":
    solution = Solution()

    test_cases = (
        ([1, 2, 5, 9], 5, 5),
        ([44, 22, 33, 11, 1], 5, 44),
        ([21212, 10101, 12121], 1000000, 1)
    )

    for i, (nums, threshold, expected) in enumerate(test_cases, 1):
        output = solution.smallestDivisor(nums, threshold)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")