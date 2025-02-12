class Solution:
    """Finds the maximum subarray"""

    # Analysis: time = O(n), space = O(1)
    def max_sub_array(self, nums: list[int]) -> int:
        """Return the sum of the maximum subarray using Kadane's Algorithm"""
        current_sum = max_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(current_sum + num, num)
            max_sum = max(current_sum, max_sum)
        
        return max_sum

if __name__ == "__main__":
    solution = Solution()

    nums1 = [-2,1,-3,4,-1,2,1,-5,4]
    assert solution.max_sub_array(nums1) == 6, "Test case 1 failed"

    nums2 = [1]
    assert solution.max_sub_array(nums2) == 1, "Test case 2 failed"

    nums3 = [5,4,-1,7,8]
    assert solution.max_sub_array(nums3) == 23, "Test case 3 failed"

    print("All test cases passed!")