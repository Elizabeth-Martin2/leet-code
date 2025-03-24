class Solution:
    """
    Returns the index of the given target in an array of distinct, sorted integers.
    If not found, returns the index where it would be inserted.
    Uses binary search to find the target or index.
    """

    # Analysis: time = O(log n), space = O(1)
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                left = mid + 1
            
            else: # nums[mid] > target
                right = mid - 1

        # Normal binary search returns -1, in this case return the correct index
        return mid + 1 if nums[mid] < target else mid
        
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1,3,5,6], 5, 2),
        ([1,3,5,6], 2, 1),
        ([1,3,5,6], 7, 4)
    ]

    for i, (test, target, expected) in enumerate(test_cases):
        output = solution.searchInsert(test, target)
        assert output == expected, f"Test case {i + 1} failed, expected {expected}, got {output}"

    print("All test cases passed!")