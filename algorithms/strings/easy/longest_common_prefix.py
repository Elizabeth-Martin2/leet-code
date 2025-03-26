class Solution:
    """
    Given a list of strings (strs), return the longest common
    prefix among the strings.

    LC. 14 Longest Common Prefix
    """

    # Analysis: time = O(m * n), space = O(n)
    # where n = len(shortest string in strs), m = number of words in strs
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        for s in strs[1:]:
            while s[:len(prefix)] != prefix and len(prefix) != 0:
                prefix = prefix[:-1]
        
        return prefix


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        (["flower","flow","flight"], "fl"),
        (["dog","racecar","car"], ""),
        (["flower","grower","mower"], "")
    ]

    for i, (words, expected) in enumerate(test_cases,1):
        output = s.longestCommonPrefix(words)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")