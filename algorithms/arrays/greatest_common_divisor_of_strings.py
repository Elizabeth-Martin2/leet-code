def gcd(str1: str, str2: str) -> int:
    """
    Returns the greatest common divisor (GCD) of the lengths of two strings.
    """
    len1, len2 = len(str1), len(str2)

    res = min(len1, len2)
    while res:
        if len1 % res == 0 and len2 % res == 0:
            return res
        res -= 1

    return res


class Solution:
    """
    Returns the greatest common divisor string of two input strings.

    The GCD string is the largest string that can be concatenated multiple
    times to form both input strings.
    """

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd_str_len = gcd(str1, str2)
        gcd_str = str1[:gcd_str_len]

        # Check if gcd_str can form both strings through repetition
        if str1 == gcd_str * (len(str1) // gcd_str_len) and str2 == gcd_str * (len(str2) // gcd_str_len):
            return gcd_str
        else:
            return ""


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("ABCABC", "ABC", "ABC"),
        ("ABABAB", "ABAB", "AB"),
        ("LEET", "CODE", ""),
        ("AAAA", "AA", "AA"),
    ]

    for i, (str1, str2, expected) in enumerate(test_cases, 1):
        assert solution.gcdOfStrings(str1, str2) == expected, f"Test case {i} failed"

    print("All test cases passed!")
