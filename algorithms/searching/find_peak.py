class Solution:
    """
    Returns the index of a peak element in a given integer array.
    Uses binary search to find the peak element.

    Guarantee: nums[i] != nums[i + 1] for all valid i
    """

    # Analysis: time = O(log n), space = O(1)
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        
        if len(nums) == 1:
            return 0

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]: 
                left = mid + 1
            else:
                right = mid

        return left
    
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1,2,1,3,5,6,4], 5),
        ([1,2,3,1], 2),
        ([6,5,4,3,2,3,2], 0),
        ([1], 0)
    ]

    for i, (test, expected) in enumerate(test_cases, 1):
        output = solution.findPeakElement(test)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")