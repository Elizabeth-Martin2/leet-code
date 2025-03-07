class Solution:
    """
    Returns the floor square root of a given number.
    Uses binary search to find the number.
    (Can't use sqrt function)
    """

    # Analysis: time = O(log n), space = O(1)
    def floorSqrt(self, n): 
        left, right = 0, (n // 2) + 1
        
        while left <= right:
            mid = (left + right) // 2 
            
            mid_sqrd = mid * mid
            if mid_sqrd == n:
                return mid 
                
            if mid_sqrd > n: 
                right = mid - 1
            
            else:
                left = mid + 1
                
        return right
    
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (74, 8), (25, 5), (1, 1), (11, 3)
    ]

    for i, (num, expected) in enumerate(test_cases, 1):
        output = solution.floorSqrt(num)
        assert output == expected, f"Test case {i} failed, exptected {expected}, got {output}"

    print("All test cases passed!")