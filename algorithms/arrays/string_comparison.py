class Solution:
    """Compresses a character array in-place using run-length encoding."""

    # Analysis: time = O(n), space = O(1)
    def compress(self, chars: list[str]) -> int:
        """Modifies chars in-place and returns the new length after compression."""
        i = 0
        j = 0

        while j < len(chars):
            char = chars[j]
            counter = 0

            while j < len(chars) and chars[j] == char:
                j += 1
                counter += 1

            chars[i] = char
            i += 1
            if counter > 1:
                for digit in str(counter):
                    chars[i] = digit
                    i += 1

        return i


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (["a", "a", "b", "b", "c", "c", "c"], ["a", "2", "b", "2", "c", "3"], 6),
        (["a"], ["a"], 1),
        (["a", "b", "c"], ["a", "b", "c"], 3),
        (["a", "a", "a", "a", "a", "b"], ["a", "5", "b"], 3),
    ]

    for i, (chars, expected_chars, expected_len) in enumerate(test_cases, 1):
        result_len = solution.compress(chars)
        assert result_len == expected_len, f"Test case {i} failed: expected length {expected_len}, got {result_len}"
        assert chars[:result_len] == expected_chars, f"Test case {i} failed: expected chars {expected_chars}, got {chars[:result_len]}"

    print("All test cases passed!")
