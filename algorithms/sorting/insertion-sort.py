# Attempt 2:
class Solution:
    def insertionSort(self, arr):
        n = len(arr)
        
        for i in range(1, n): # O(n)
            key = arr[i]
            j = i - 1 # starts at position 0
            
            while j >= 0 and arr[j] > key: # O(n)
                arr[j + 1] = arr[j]
                j -= 1
            
            arr[j + 1] = key

# Analysis: O(n^2)

# Attempt 1: 
# Optimized, but technically not insertion sort
# this implementation swaps instead of shifts
# class Solution:
#     def insertionSort(self, arr):
#         n = len(arr)
        
#         for i in range(1, n): # O(n)
#             for j in range(0, i): # O(n)
#                 if arr[i] < arr[j]:
#                     arr[i], arr[j] = arr[j], arr[i]

# # Analysis: O(n^2)