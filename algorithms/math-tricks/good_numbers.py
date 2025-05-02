class Solution:
    """
    A digit string is good if the digits (0-indexed) at even
    indices are even and the digits at odd indices are prime
    (2, 3, 5, or 7).

    Given an integer n, return the total number of good digit
    strings of length n. Since the answer may be large,
    return it modulo 109 + 7.

    LC. 1922 Count Good Numbers
    """

    # Analysis: time = O(n), space = O(n) [due to recursive call stack]
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        # Key observations:
        # If index is even: you have 5 valid digits to choose from
        # If index is odd: you have 4 valid digits to choose from
        def countGood(i):
            if i == n:
                return 1
            if i % 2 == 0:
                return (5 * countGood(i + 1)) % MOD
            else:
                return (4 * countGood(i + 1)) % MOD

        return countGood(0)
    

if __name__ == "__main__":
    s = Solution()
    test_cases = [
        (1, 5),
        (4, 400),
        (50, 564908303)
    ]

    for i, (n, expected) in enumerate(test_cases, 1):
        output = s.countGoodNumbers(n)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")