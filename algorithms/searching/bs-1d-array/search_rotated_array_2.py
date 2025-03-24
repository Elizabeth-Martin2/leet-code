class Solution:
    """
    Returns a boolean value representing if the target value is present
    in the sorted and possibly rotated integer array.
    Uses binary search to find the target value.
    """

    # Analysis: time = O(log n), space = O(1)
    def search(self, nums: list[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        if len(nums) == 1:
            return True if nums[0] == target else False

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True

            # Handles non-distinct values
            while nums[left] == nums[mid] and left < mid:
                left += 1
            while nums[right] == nums[mid] and right > mid:
                right -= 1

            if nums[left] <= nums[mid]:
                # left is sorted half
                if nums[left] <= target < nums[mid]:
                    # target is in sorted half
                    right = mid - 1
                else:
                    # target is in unsorted half (right)
                    left = mid + 1
            
            else: # right half is sorted half
                if nums[mid] < target <= nums[right]:
                    # target is in sorted half
                    left = mid + 1
                else:
                    # target is in unsorted half (left)
                    right = mid - 1

        return False

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1,1,1,1,1,1,1,1,1,13,1,1,1,1,1,1,1,1,1,1,1,1], 13, True),
        ([1], 0, False),
        ([1,0,1,1,1], 0, True),
        ([2,5,6,0,0,1,2], 3, False),
        ([2,5,6,0,0,1,2], 0, True)
    ]

    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = solution.search(nums, target)
        assert result == expected, f"Test case {i} failed: {nums}, target={target}, expected {expected}, got {result}"

    print("All test cases passed!")
