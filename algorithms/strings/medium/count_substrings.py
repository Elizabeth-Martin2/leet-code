from collections import defaultdict

class Solution:
    """
    Given a string s of lowercase alphabets, count all possible
    substrings (not necessarily distinct) that have exactly k
    distinct characters.
    """

    # Overall Analysis: time = O(n), space = O(n)
    def countSubstr(self, s, k):
        return self.atMostKDistinct(s, k) - self.atMostKDistinct(s, k - 1)

    def atMostKDistinct(self, s, k):
        count = defaultdict(int)
        start = 0
        res = 0

        for end in range(len(s)):
            count[s[end]] += 1

            while len(count) > k:
                count[s[start]] -= 1
                if count[s[start]] == 0:
                    del count[s[start]]
                start += 1

            res += end - start + 1

        return res


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("aba", 2, 3),
        ("abaaca", 1, 7),
        ("cdad", 4, 0)
    ]

    for i, (s, k, expected) in enumerate(test_cases, 1):
        output = solution.countSubstr(s, k)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")
