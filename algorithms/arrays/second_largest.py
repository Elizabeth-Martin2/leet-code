class Solution:
    """Finds the second largest integer in the array"""

    # Analysis: O(n)
    def get_second_largest(self, arr: list[int]) -> int:
        largest = second_largest = -1
        
        for num in arr: # O(n)  
            if num > largest:
                second_largest = largest
                largest = num
            if num > second_largest and num != largest:
                second_largest = num
        
        return second_largest
                

if __name__ == "__main__":
    arr1 = [12, 35, 1, 10, 34, 1]
    arr1_seond_largest = Solution().get_second_largest(arr1)
    print(f"Array1: {arr1}; second largest integer: {arr1_seond_largest}")
    
    arr2 = [10, 5, 10]
    arr2_seond_largest = Solution().get_second_largest(arr2)
    print(f"Array1: {arr2}; second largest integer: {arr2_seond_largest}")
    
    arr3 = [10, 10, 10]
    arr3_seond_largest = Solution().get_second_largest(arr3)
    print(f"Array3: {arr3}; second largest integer: {arr3_seond_largest}")
