class Solution:
    # Function to sort an array with insertion algorithm
    # Analysis: O(n^2)
    def insertionSort(self, arr):
        n = len(arr)
        
        for i in range(1, n): # O(n)
            key = arr[i]
            j = i - 1 # starts at position 0
            
            while j >= 0 and arr[j] > key: # O(n)
                arr[j + 1] = arr[j]
                j -= 1
            
            arr[j + 1] = key

    # Function to sort an array with recursive insertion algorithm
    # Analysis: O(n^2)
    def recInsertionSort(self, arr, n = None):
        if n == None:
            n = 1
        # Base case -- sorted
        if n == len(arr):
            return
        
        # Assume n - 1 elements are already sorted
        j = n - 1
        key = arr[n]
        while j >= 0 and arr[j] > key: # O(n)
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        self.recInsertionSort(arr, n + 1) # O(n)
