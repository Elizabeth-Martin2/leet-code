# Attempt 1: O(n log n)
class Solution:
    def merge(self, arr, l, mid, r): # O(n)
        l_arr = arr[l: mid + 1]
        r_arr = arr[mid + 1: r + 1]
        
        i = j = 0
        k = l
        
        # Sort left and right arrays, then merge
        while i < len(l_arr) and j < len(r_arr): # O(n)
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
    def mergeSort(self,arr, l, r):
        if l < r:
            mid = (l + r) // 2
            # Left call
            self.mergeSort(arr, l, mid)
            # Right call
            self.mergeSort(arr, mid + 1, r) 
        
            self.merge(arr, l, mid, r)