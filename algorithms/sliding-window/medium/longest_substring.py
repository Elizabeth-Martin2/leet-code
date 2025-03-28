class Solution:
    """
    Given a string (s) return the length of the longest
    substring without duplicate characters.
    """

    # Analysis: time = O(n), space = O(1)
    # where n = len(s)
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, max_len = 0, 0
        seen = set()

        for end in range(len(s)):
            while s[end] in seen:
                seen.remove(s[start])
                start += 1

            seen.add(s[end])
            max_len = max(max_len, end - start + 1)
    
        return max_len


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3)
    ]

    for i, (s, expected) in enumerate(test_cases, 1):
        output = solution.lengthOfLongestSubstring(s)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")