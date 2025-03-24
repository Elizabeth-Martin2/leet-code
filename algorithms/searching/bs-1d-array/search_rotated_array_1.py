class Solution:
    """
    Returns the index of the target value in a sorted and possibly
    rotated array of distinct integers.
    Uses binary search to locate the target value.
    """

    # Analysis: time = O(log n), space = O(1)
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                # left half is sorted
                if nums[left] <= target < nums[mid]:
                    # target is in sorted half
                    right = mid - 1
                else:
                    # target is in unsorted half
                    left = mid + 1
            
            else: # right half is sorted
                if nums[mid] < target <= nums[right]:
                    # target is in sorted half
                    left = mid + 1
                else:
                    # target is in unsorted half
                    right = mid - 1

        return -1
    
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([4,5,6,7,0,1,2], 0, 4),
        ([4,5,6,7,0,1,2], 3, -1),
        ([1], 0, -1),
        ([7,0,1,2,3,4,5,6], 0, 1)
    ]

    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = solution.search(nums, target)
        assert result == expected, f"Test case {i} failed: {nums}, target={target}, expected {expected}, got {result}"

    print("All test cases passed!")
