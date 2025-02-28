class Solution:
    """Performs binary search in a sorted array."""

    # Analysis: time = O(log n), space = O(log n)
    def rec_bin_search(self,arr: list[int], k: int, left: int = 0, right: int = None) -> int:
        """
        Returns the index of the target value in an integer array.
        Searches using recursive binary search.
        """

        if right is None: # Catch first run with default input
            right = len(arr) - 1
        
        if left > right:
            return -1
        
        mid = (left + right) // 2

        if arr[mid] == k:
            return mid
        
        # Recursive calls for right & left side (respectively)
        # Note: avoid passing sliced array as it creates new arrays and adds to space complexity
        if arr[mid] < k:
            return self.rec_bin_search(arr, k, mid + 1, right)
        else:
            return self.rec_bin_search(arr, k, left, mid - 1)

    # Analysis: time = O(log n), space = O(1)
    def bin_search(self, nums: list[int], target: int) -> int:
        """
        Returns the index of the target value in an integer array.
        Searches using binary search.
        """
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1, 2, 3, 4, 5, 6], 6, 5),
        ([2, 5, 6, 9, 12], 4, -1),
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1)
    ]

    for i, (test, target, expected) in enumerate(test_cases):
        assert (it_output := solution.bin_search(test, target)) == expected, f"Iterative test case {i + 1} failed, expected: {expected}, got: {it_output}"
        assert (rec_output := solution.rec_bin_search(test, target)) == expected, f"Recursive test case {i + 1} failed, expected: {expected}, got: {rec_output}"

    print("All test cases passed!")
