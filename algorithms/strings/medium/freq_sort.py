class Solution:
    """
    Given a string (s) return the string with the characters
    rearranged based on their frequency in descending order.

    LC. 451 Sort Characters by Frequency
    """

    # Analysis: time = O(n), space = O(n)
    # where n = len(s)
    def frequencySort(self, s: str) -> str:
        # Base case
        if len(s) < 3:
            return s
        
        char_count = {}

        for letter in s:
            char_count[letter] = char_count.get(letter, 0) + 1

        max_freq = max(char_count.values())
        buckets = [[] for _ in range(max_freq + 1)]

        for ch, freq in char_count.items():
            buckets[freq].append(ch)

        res = []
        for freq in range(len(buckets) - 1, 0, -1):
            for ch in buckets[freq]:
                res.append(ch * freq)

        # Below also worked, but causes runtime to increase to O(n log k)
        # where n = len(s) and k = num unique characters

        # char_count = sorted(char_count.items(), key = lambda item: item[1], reverse = True)
        # for letter, freq in char_count:
        #     res += letter * freq

        return "".join(res)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("tree", "eetr"),
        ("cccaaa", "cccaaa"),
        ("Aabb", "bbAa")
    ]

    for i, (s, expected) in enumerate(test_cases, 1):
        output = solution.frequencySort(s)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")