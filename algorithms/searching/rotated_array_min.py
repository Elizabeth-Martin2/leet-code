class Solution:
    """
    Returns the minimum integer in a sorted, distinct, and possibly
    rotated array of integers.
    Uses binary search to find the minimum integer.
    """

    # Analysis: time = O(log n), space = O(1)
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        nums_min = float("inf")

        while left <= right:
            mid = (left + right) // 2
            
            nums_min = min(nums[mid], nums_min)

            if nums[mid] > nums[right]:
                # pivot is to the right
                left = mid + 1
            
            else:
                # pivot is to the left
                right = mid - 1
        
        return nums_min


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([4,5,6,7,0,1,2], 0),
        ([4,5,7,1,2], 1),
        ([1], 1),
        ([7,0,1,2,3,4,5,6], 0)
    ]

    for i, (test, expected) in enumerate(test_cases, 1):
        output = solution.findMin(test)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")