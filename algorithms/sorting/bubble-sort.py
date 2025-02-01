# Attempt 2: Optimized solution
class Solution:
    def bubbleSort(self,arr):
        n = len(arr)
        for i in range(n - 1): # O(n)
            swapped = False
            
            for j in range(n - 1 - i): # O(n)
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            
            if swapped == False:
                break

# Analysis: O(n^2)


# Attempt 1: Passed test cases -- not optimized
# class Solution:
#     def bubbleSort(self,arr):
#         current_max = 0
#         unsorted_portion = n = len(arr) - 1
        
        
#         for i in range(len(arr)): # O(n)
#             # Search for max
#             for ind, num in enumerate(arr[0:unsorted_portion + 1]): # O(n - unsorted) == O(n)
#                 if num >= current_max:
#                     current_max = num
#                     current_max_ind = ind
#             # print(current_max)
                
#             for ind in range(current_max_ind, unsorted_portion):  # O(n)
#                 # print(arr)
#                 arr[ind], arr[ind + 1] = arr[ind + 1], arr[ind] # swap with neighbor
#                 # print(arr)
            
#             unsorted_portion -= 1
#             current_max = 0    
            
# Analysis: O(n^2)