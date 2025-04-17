class Solution:
    """
    Given an array of non-empty strings, return an answer array of
    the same size where answer[i] is the shortest substring of arr[i]
    that does not occur as a substring in any other string in arr.

    Note: If there are multiple substrings, answer[i] should be the
    lexicographically smallest.

    LC. 3076 Shortest Uncommon Substring in an Array
    """

    # TODO: Come back and optimize this

    # Helper function analysis:
    # time = O(m^2 * log m^2), space = O(m^2)
    # where m = average length of string
    def genSubstrings(self, substring: str) -> list[str]:
        res = []

        for i in range(len(substring)):
            for j in range(i + 1, len(substring) + 1):
                res.append(substring[i:j])

        return sorted(res, key = lambda x: (len(x), x))


    # Brute force analysis: time = O(n^2 * m^3), space = O(n * m^2)
    # where n = number of strings in arr
    def shortestSubstrings(self, arr: list[str]) -> list[str]:
        answer = [""] * len(arr)

        for i, s in enumerate(arr): # n
            substrings = self.genSubstrings(s) # O(m^2 * log m^2)

            other_strs = arr[:i] + arr[i + 1:]  # O(n)

            found = False
            for substring in substrings:  # O(m^2)
                if all(substring not in o for o in other_strs): # O(n * m)
                    answer[i] = substring
                    found = True
                    break

            if not found:
                answer[i] = ""

        return answer


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        (["cab","ad","bad","c"], ["ab","","ba",""]),
        (["abc","bcd","abcd"], ["","","abcd"])
    ]

    for i, (input, expected) in enumerate(test_cases, 1):
        result = s.shortestSubstrings(input)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"

    print("All test cases passed!")
