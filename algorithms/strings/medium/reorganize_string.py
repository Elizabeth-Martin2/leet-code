from collections import Counter

class Solution:
    """
    Given a string s, rearrange the characters of s so that any
    two adjacent characters are not the same.

    LC. 767 Reorganize String
    """

    # Analysis: time = O(n), space = O(1)
    # where n = len(s)
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        n = len(s)
        most_freq = max(counter.values())

        if most_freq > (n + 1) // 2:
            return ""

        sorted_counter = sorted(counter.items(), key=lambda x: -x[1])

        res = [""] * n
        idx = 0
        for key, freq in sorted_counter:
            for i in range(freq):
                res[idx] = key
                idx += 2
                if idx >= n:
                    idx = 1
            

        return ''.join(res)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("ogccckcwmbmxtsbmozli", "cbcgckcwmxmtmsozolbi"),
        ("vvvlo", "vlvov"),
        ("aaab", ""),
        ("aab", "aba")
    ]

    for i, (input, expected) in enumerate(test_cases, 1):
        output = solution.reorganizeString(input)
        assert output == expected, f"Test case {i} failed: expected {expected}, got {output}"

    print("All test cases passed!")
