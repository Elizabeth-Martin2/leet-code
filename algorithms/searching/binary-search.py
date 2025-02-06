class Solution:
    """Performs binary search in a sorted array recursively."""

    # Analysis: time = O(log n), space = O(log n)
    def search_in_sorted(self,arr: list[int], k: int, left: int = 0, right: int = None) -> bool:
        """Recursively search for k in a sorted array using binary search."""

        if right is None: # Catch first run with default input
            right = len(arr) - 1
        
        if left > right:
            return False
        
        mid = (left + right) // 2

        if arr[mid] == k:
            return True
        
        # Recursive calls for right & left side (respectively)
        # Note: avoid passing sliced array as it creates new arrays and adds to space complexity
        if arr[mid] < k:
            return self.search_in_sorted(arr, k, mid + 1, right)
        else:
            return self.search_in_sorted(arr, k, left, mid - 1)


if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5, 6]
    k = 6
    print(f"Nums1: {nums1}, k = {k}.  Present in array: {Solution().search_in_sorted(nums1, k)}")

    nums2 = [2, 5, 6, 9, 12]
    k = 4
    print(f"Nums2: {nums2}, k = {k}.  Present in array: {Solution().search_in_sorted(nums2, k)}")

