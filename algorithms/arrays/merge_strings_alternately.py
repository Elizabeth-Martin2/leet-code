class Solution:
    """Merges two words alternately."""

    # Analysis: time = O(n), space = O(n)
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_str = []
        i = 0

        while i < len(word1) and i < len(word2):
            merged_str.append(word1[i])
            merged_str.append(word2[i])
            i += 1

        merged_str.append(word1[i:] or word2[i:])
        return "".join(merged_str)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("abc", "pqr", "apbqcr"),
        ("ab", "pqrs", "apbqrs"),
        ("abcd", "pq", "apbqcd"),
        ("", "xyz", "xyz"),
    ]

    for i, (word1, word2, expected) in enumerate(test_cases, 1):
        assert solution.mergeAlternately(word1, word2) == expected, f"Test case {i} failed"

    print("All test cases passed!")
