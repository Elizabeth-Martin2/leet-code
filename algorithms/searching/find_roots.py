class Solution:
    # Analysis: time = O(log n), space = O(1)
    def floorSqrt(self, n: int) -> int:
        """
        Returns the floor square root of a given number.
        Uses binary search to find the number.
        (Can't use sqrt function)
        """
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

    # Analysis: time = O(log m), space = O(1)
    def nthRoot(self, n: int, m: int) -> int:
        """
        Return the nth root of m.  If it's not an integer,
        returns -1.
        Uses binary search to find the root.
        """
        left, right = 1, m

        while left <= right:
            mid = (left + right) // 2
            mid_power = mid ** n

            if mid_power == m:
                return mid

            if mid_power < m:
                left = mid + 1
            else:
                right = mid - 1

        return -1
    
if __name__ == "__main__":
    solution = Solution()
    floor_root_tests = [
        (74, 8), (25, 5), (1, 1), (11, 3)
    ]
    n_root_tests = [
        (3, 27, 3),
        (2, 16, 4),
        (3, 9, -1),
        (4, 81, 3),
    ]

    for i, (num, expected) in enumerate(floor_root_tests, 1):
        output = solution.floorSqrt(num)
        assert output == expected, f"Floor root test case {i} failed, exptected {expected}, got {output}"

    for i, (power, base, expected) in enumerate(n_root_tests, 1):
        output = solution.nthRoot(power, base)
        assert output == expected, f"Nth-root test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")