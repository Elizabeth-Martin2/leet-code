class Solution:
    """
    Implement the pow(x, n) function which calculates
    x raised to the power n.

    LC. 50 Pow(x,n)
    """

    # Recurisve analysis:
    # time = O(log n), space = O(log n)
    def myPow(self, x: float, n: int) -> float:
        def fastPow(x: float, n: int) -> float:
            if n == 0:
                return 1
            
            half = fastPow(x, n//2)
            return half * half if n % 2 == 0 else half * half * x
        
        if n < 0:
            x = 1/x
            n = -n
        return fastPow(x, n)


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        (3, 2, 9),
        (25, 10, 95367431640625),
        (130, 10, 1378584918490000000000)
    ]

    for i, (x, n, expected) in enumerate(test_cases, 1):
        output = s.myPow(x, n)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")