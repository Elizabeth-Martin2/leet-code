class Solution:
    """
    Determines if two strings are isomorphic and returns
    boolean value accordingly.

    Note: Two strings s and t are isomorphic if the
    characters in s can be replaced to get t.

    LC. 205 Isomorphic Strings
    """

    # Analysis: time = O(n), space = O(n)
    # where n = len(s)
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s_t = {}
        map_t_s = {}

        for ch_s, ch_t in zip(s, t):
            if ch_s in map_s_t and map_s_t[ch_s] != ch_t:
                return False
            if ch_t in map_t_s and map_t_s[ch_t] != ch_s:
                return False
            map_s_t[ch_s] = ch_t
            map_t_s[ch_t] = ch_s

        return True

if __name__ == "__main__":
    s = Solution()

    test_cases = [
        ("egg", "add", True),
        ("foo", "bar", False),
        ("paper", "title", True),
        ("ab", "aa", False),
        ("aba", "xyx", True),
        ("aba", "xyy", False),
        ("a", "a", True),
        ("", "", True),
    ]

    for i, (s_input, t_input, expected) in enumerate(test_cases,1):
        output = s.isIsomorphic(s_input, t_input)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output} for ({s_input}, {t_input})"

    print("All test cases passed!")
