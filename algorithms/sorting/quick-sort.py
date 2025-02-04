class Solution:
    """Implements QuickSort algorithm using last element as pivot"""

    # Analysis: O(n log n)
    def quick_sort(self, arr: list[int], low: int, high: int) -> None:
        """Sorts arr[low, high + 1] in-place using Quicksort"""
        if low >= high:
            return
        
        pivot_index = self.partition(arr, low, high)
        
        # Each level processes O(n), depth is O(log n), so total O(n log n)
        self.quick_sort(arr, low, pivot_index - 1)
        self.quick_sort(arr, pivot_index + 1, high)

    def partition(self, arr: list[int], low: int, high: int) -> int:
        """Partitions array around pivot and returns pivot index"""
        pivot = arr[high]  
        i = low - 1  
        for j in range(low, high):  # O(n)
            if arr[j] < pivot:
                # This keeps track of where the pivot will go
                i += 1
                # Swap arr[i] and arr[j] to move smaller elements left
                arr[i], arr[j] = arr[j], arr[i] 
            
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1


if __name__ == "__main__":
    arr = [4, 1, 2, 5, 7, 9]
    print(f"Unsorted array: {arr}")

    n = len(arr) - 1
    Solution().quick_sort(arr, 0, n)

    print(f"Sorted array: {arr}")
