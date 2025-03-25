class Solution:
    def reverseWords(self, s: str) -> str:
        split = s.split()

        return " ".join(split[::-1])
    

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("the sky is blue", "blue is sky the"),
        ("a good  example", "example good a"),
        (" hello world ", "world hello")
    ]

    for i, (words, expected) in enumerate(test_cases, 1):
        output = solution.reverseWords(words)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")