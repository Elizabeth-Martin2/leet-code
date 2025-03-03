class Solution:
    """Reverses the vowels in a string while preserving order of other characters."""

    # Analysis: time = O(n), space = O(n)
    def reverseVowels(self, s: str) -> str:
        vowels = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
        s_list = list(s)

        first_ptr, last_ptr = 0, len(s) - 1

        while first_ptr < last_ptr:
            if s_list[first_ptr] in vowels and s_list[last_ptr] in vowels:
                s_list[first_ptr], s_list[last_ptr] = s_list[last_ptr], s_list[first_ptr]
                first_ptr += 1
                last_ptr -= 1

            if s_list[first_ptr] not in vowels:
                first_ptr += 1

            if s_list[last_ptr] not in vowels:
                last_ptr -= 1

        return "".join(s_list)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("hello", "holle"),
        ("leetcode", "leotcede"),
        ("aA", "Aa"),  # Case sensitivity check
        ("xyz", "xyz"),  # No vowels
    ]

    for i, (s, expected) in enumerate(test_cases, 1):
        assert solution.reverseVowels(s) == expected, f"Test case {i} failed"

    print("All test cases passed!")
