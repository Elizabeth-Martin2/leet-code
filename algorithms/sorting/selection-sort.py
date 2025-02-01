#User function Template for python3

class Solution: 
    def selectionSort(self, arr):
        unsorted_ind = current_min = 0
        n = len(arr)
        
        while unsorted_ind < n - 1: # O(n)
            current_min = min(arr[unsorted_ind:])  # O(n - unsorted_ind) == O(n)
            current_min_ind = (arr[unsorted_ind:].index(current_min)) + unsorted_ind

            arr[unsorted_ind], arr[current_min_ind] = arr[current_min_ind], arr[unsorted_ind]
            unsorted_ind += 1

# Analysis: O(n^2)

# Optimization:
# class Solution: 
#     def selectionSort(self, arr):
#         n = len(arr)
        
#         for i in range(n - 1):  # O(n)
#             min_index = i 
            
#             for j in range(i + 1, n):  
#                 if arr[j] < arr[min_index]:
#                     min_index = j
            
#             # Swap only if needed
#             if min_index != i:
#                 arr[i], arr[min_index] = arr[min_index], arr[i]
