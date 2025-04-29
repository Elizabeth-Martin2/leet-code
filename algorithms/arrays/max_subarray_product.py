class Solution:
    """
    Given an array of integers nums and an integer k, return the number
    of contiguous subarrays where the product of all the elements in
    the subarray is strictly less than k.

    LC. 713 Subarray Product Less than K
    """

    # Analysis: time = O(n), space = O(1)
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k == 0:
            return 0
        
        count = 0
        left = 0
        current_prod = 1

        for right in range(len(nums)):
            current_prod *= nums[right]

            while current_prod >= k and left <= right:
                current_prod /= nums[left]
                left += 1
            
            count += (right - left + 1)

        return count


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([10,5,2,6], 100, 8),
        ([1,2,3], 0, 0),
        ([10,5,2,6,3,8,12], 1000, 21)
    ]

    for i, (nums, k, expected) in enumerate(test_cases, 1):
        assert solution.numSubarrayProductLessThanK(nums, k) == expected, f"Test case {i} failed"

    print("All test cases passed!")