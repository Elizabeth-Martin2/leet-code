class Solution:
    """
    Return the number of invesions in an array of integers.

    Inversion Count: For an array, inversion count indicates how
    far (or close) the array is from being sorted. If the array
    is already sorted then the inversion count is 0.
    """

    # Merge_and_count analysis: time = O(n), space = O(n)
    def merge_and_count(self, arr: list[int], left: int, mid:int, right:int) -> int:
        """Helper function to merge arrays together and count inversions"""

        left_half = arr[left : mid + 1]
        right_half = arr[mid + 1: right + 1]
        
        i = j = 0
        k = left
        inv_count = 0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
                inv_count += (mid - left + 1 - i)
            k += 1
        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k +=1
        
        return inv_count
    
    # Overall analysis: time = O(n log n), space = O(n)
    def inversionCount(self, arr: list[int], left:int = 0, right:int = None) -> int:
        """Count inversions with merge sort"""

        if right is None:
            if not arr:
                return 0
            right = len(arr) - 1
            
        if left < right: 
            mid = (left + right) // 2
            
            left_inv = self.inversionCount(arr, left, mid)
            right_inv = self.inversionCount(arr, mid + 1, right)
            merge_inv = self.merge_and_count(arr, left, mid, right)
            
            return left_inv + right_inv + merge_inv
        
        return 0
        
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([2, 4, 1, 3, 5], 3),
        ([2, 3, 4, 5, 6], 0),
        ([6, 5, 4, 3, 2, 1], 15)
    ]

    for i, (test, expected) in enumerate(test_cases):
        output = solution.inversionCount(test)
        assert output == expected, f"Test case {i + 1} failed, expected {expected} got {output}"

    print("All test cases passed!")