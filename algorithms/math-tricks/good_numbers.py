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

    # Optimized attempt
    # Analysis: time: O(log n), space = O(log n)
    def countGoodNumbersOpt(self, n: int) -> int:
        MOD = 10**9 + 7

        def mod_pow(x, power):
            if power == 0:
                return 1
            half = mod_pow(x, power // 2)
            result = (half * half) % MOD
            if power % 2 == 1:
                result = (result * x) % MOD
            return result

        even_count = (n + 1) // 2
        odd_count = n // 2

        return (mod_pow(5, even_count) * mod_pow(4, odd_count)) % MOD


    # First attempt -- not efficient enough
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