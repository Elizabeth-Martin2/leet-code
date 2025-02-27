class Solution:
    """Classic implementation of merge sort"""

    # Analysis: time = O(n log n), space = O(n)
    def merge(self, arr: list[int], l:int, mid:int, r:int):
        # Slicing arrays brings space complexity up to O(n)
        l_arr = arr[l: mid + 1]
        r_arr = arr[mid + 1: r + 1]

        i = j = 0
        k = l

        # Merge left & right arrays while sorting
        while i < len(l_arr) and j < len(r_arr):
            if l_arr[i] <= r_arr[j]:
                arr[k] = l_arr[i]
                i += 1
            else:
                arr[k] = r_arr[j]
                j += 1
            k += 1

        while i < len(l_arr): # O(n/2) (worst case)
            arr[k] = l_arr[i]
            i += 1
            k += 1
        while j < len(r_arr): # O(n/2) (worst case)
            arr[k] = r_arr[j]
            j += 1
            k += 1

    # O(log n) because of continuously dividing array in half
    def mergeSort(self,arr: list[int], l:int = 0, r:int = None):
        if r is None:
            r = len(arr) - 1

        if l < r:
            mid = (l + r) // 2
            # Left call
            self.mergeSort(arr, l, mid)
            # Right call
            self.mergeSort(arr, mid + 1, r)

            self.merge(arr, l, mid, r)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1,3,2,3,1], [1,1,2,3,3]),
        ([2,4,3,5,1], [1,2,3,4,5]),
        ([10,9,8,7,6,5,4,3,2,1], [1,2,3,4,5,6,7,8,9,10])
    ]

    for i, (test, expected) in enumerate(test_cases):
        solution.mergeSort(test)
        assert test == expected, f"Test case {i + 1} failed, expected {expected}, got {test}"

    print("All test cases passed!")