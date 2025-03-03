class Solution:
    """Reverses the order of words in a string."""

    # Analysis: time = O(n), space = O(n)
    def reverseWords(self, s: str) -> str:
        """Returns a string with words reversed while maintaining spaces."""
        return " ".join(s.split()[::-1])


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("the sky is blue", "blue is sky the"),
        ("  hello world  ", "world hello"),
        ("a good   example", "example good a"),
        ("singleword", "singleword"),
        ("", ""),
    ]

    for i, (s, expected) in enumerate(test_cases, 1):
        assert solution.reverseWords(s) == expected, f"Test case {i} failed"

    print("All test cases passed!")
