class Solution:
    """
    Returns the minimum integer and its index in a sorted,
    distinct, and possibly rotated array of integers.

    Note: the index of the minimum integer in a rotated array
    is equivalent to the number of times the array was rotated.

    Uses binary search to find the minimum integer.
    """

    # Analysis: time = O(log n), space = O(1)
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        nums_min, nums_min_ind = float("inf"), -1

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] < nums_min:
                nums_min = nums[mid]
                nums_min_ind = mid

            if nums[mid] > nums[right]:
                # pivot is to the right
                left = mid + 1
            
            else:
                # pivot is to the left
                right = mid - 1
        
        return nums_min, nums_min_ind


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([4,5,6,7,0,1,2], 0, 4),
        ([4,5,7,1,2], 1, 3),
        ([1], 1, 0),
        ([7,0,1,2,3,4,5,6], 0, 1)
    ]

    for i, (test, expected_min, expected_rotation_ind) in enumerate(test_cases, 1):
        output_min, output_rotation_ind = solution.findMin(test)
        assert output_min == expected_min, f"Test case {i} failed, expected {expected_min}, got {output_min}"
        assert output_rotation_ind == expected_rotation_ind, f"Test case {i} failed, expected {expected_rotation_ind}, got {output_rotation_ind}"

    print("All test cases passed!")