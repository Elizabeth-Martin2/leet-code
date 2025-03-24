class Solution:
    """
    Returns the only single integer in an array of sorted 
    and duplicated integers.
    Uses binary search to find the single integer.

    Guarantee: Every element appears exactly twice, except
    for one element which appears exactly once
    """

    # Analysis: time = O(log n), space = O(1)
    def singleNonDuplicate(self, nums: list[int]) -> int:
        # Key insight: every couple starts at an even index
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2

            # Reset mid to an even index
            if mid % 2 == 1:
                mid -= 1

            # Check if mid is the first of its couple
            # if it is, single int is to the right
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            
            else:
                right = mid

        return nums[left]

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1,1,2,3,3,4,4,8,8], 2),
        ([3,3,7,7,10,11,11], 10),
        ([1,1,2], 2),
        ([1,1,2,2,3], 3)
    ]

    for i, (test, expected) in enumerate(test_cases, 1):
        output = solution.singleNonDuplicate(test)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")