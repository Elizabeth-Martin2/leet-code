class Solution:
    """
    Convert a string to a 32-bit signed integer.

    LC. 8 String to Integer (atoi)
    """

    # Analysis: time = O(n), space = O(1)
    # where n = len(s)
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # Trim leading whitespace
        if not s:
            return 0

        sign = 1
        i = 0

        # Handle sign
        if s[0] in "+-":
            if s[0] == "-":
                sign = -1
            i += 1

        # Parse digits 
        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        # Check the size and bring within limits if needed
        num *= sign
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        return max(INT_MIN, min(INT_MAX, num))


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("42", 42),
        ("   -042", -42),
        ("1337c0d3", 1337),
        ("0-1", 0),
        ("words and 987", 0)
    ]

    for i, (s, expected) in enumerate(test_cases, 1):
        output = solution.myAtoi(s)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")