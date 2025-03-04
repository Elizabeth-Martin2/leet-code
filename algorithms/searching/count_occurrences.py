class Solution:
    """
    Returns the number of occurrences of a given target in a sorted array of integers.
    Uses binary search to find the start & end indices of the target value.
    """
    
    # Analysis: time = O(log n), space = O(1)
    def binSearch(self, arr: list[int], target: int, find_first: bool) -> int:
        left, right = 0, len(arr) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == target:
                result = mid
                if find_first:
                    right = mid - 1
                else:
                    left = mid + 1
            
            elif arr[mid] > target:
                right = mid - 1
            
            else: # arr[mid] < target
                left = mid + 1
                
        return result
    
    def countFreq(self, arr, target):
        start = self.binSearch(arr, target, True)
        end = self.binSearch(arr, target, False)
        
        return end - start + 1 if start != -1 else 0


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1, 1, 2, 2, 2, 2, 3], 2, 4),
        ([1, 1, 2, 2, 2, 2, 3], 4, 0),
        ([8, 9, 10, 12, 12, 12], 12, 3)
    ]

    for i, (test, target, expected) in enumerate(test_cases, 1):
        output = solution.countFreq(test, target)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test caess passed!")