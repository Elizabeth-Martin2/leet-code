class Solution:
    """
    Given a string of roman numerals, convert it to an integer.

    LC. 13 Roman to Integer
    """

    # Analysis: time = O(n), space = O(1)
    # where n = len(s)
    def romanToInt(self, s: str) -> int:
        roman_dict = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}

        s_len = len(s)
        if s_len == 1:
            return roman_dict[s]
        
        res = 0
        for i in range(s_len):
            if i < s_len - 1 and roman_dict[s[i]] < roman_dict[s[i + 1]]:
                res -= roman_dict[s[i]]
            else:
                res += roman_dict[s[i]]

        return res


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("MMMXLV", 3045)
    ]

    for i, (s, expected) in enumerate(test_cases, 1):
        output = solution.romanToInt(s)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")