from collections import defaultdict

class Solution:
    """
    The beauty of a string is the difference in frequencies
    between the most frequent and least frequent characters.
    Given a string s, return the sum of beauty of all of its
    substrings.

    LC. 1781 Sum of Beauty of All Substrings
    """

    # Analysis: time = O(n^2), space = O(1)
    def beautySum(self, s: str) -> int:
        res = 0        
        
        for i in range(len(s)):
            count = defaultdict(int)
            for j in range(i, len(s)):
                count[s[j]] += 1
                res += max(count.values()) - min(count.values())

        return res


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("aabcb", 5),
        ("aabcbaa", 17),
        ("cdad", 2)
    ]

    for i, (s, expected) in enumerate(test_cases, 1):
        output = solution.beautySum(s)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")