class Solution:
    """
    Returns the starting and ending indices of a given target value in a
    list of sorted integers.  Returns [-1, -1] if not present.
    Uses binary search to find the indices.
    """

    # Analysis: time = O(log n), space = O(1)
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def binarySearchBoundary(find_start: bool = True) -> int:
            left, right = 0, len(nums) - 1
            location = -1

            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    location = mid
                    if find_start:
                        right = mid - 1
                    else:
                        left = mid + 1
                
                elif nums[mid] < target:
                    left = mid + 1
                
                else: # nums[mid] > target
                    right = mid - 1
            
            return location

        return [binarySearchBoundary(True), binarySearchBoundary(False)]

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([5,7,7,8,8,10], 8, [3, 4]),
        ([5,7,7,8,8,10], 6, [-1, -1]),
        ([1,2,2,3,4,4,4,5,6], 4, [4, 6]),
        ([], 0, [-1, -1])
    ]

    for i, (test, target, expected) in enumerate(test_cases, 1):
        output = solution.searchRange(test, target)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")