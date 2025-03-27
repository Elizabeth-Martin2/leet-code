class Solution:
    """
    Determine if two given strings (s, t) are anagrams of each other
    and return boolean value accordingly.

    Note: Anagrams are a word or phrase formed by rearranging the
    letters of a different word or phrase, using all the original
    letters exactly once.

    LC. 242 Valid Anagram
    """

    # Analysis: time = O(n), space = O(1)
    # where n is the number of characters in s
    # Note: space is O(1) because of fixed alphabet size
    def isAnagram(self, s: str, t: str) -> bool:
        s_len, t_len = len(s), len(t)
        
        # Base cases
        if s_len != t_len:
            return False
        if s == t:
            return True
        
        char_count = {}

        for letter in range(s_len):
            char_count[s[letter]] = char_count.get(s[letter], 0) + 1
            char_count[t[letter]] = char_count.get(t[letter], 0) - 1

        for key, value in char_count.items():
            if value != 0:
                return False        

        return True


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("flower", "", False)
    ]

    for i, (s, t, expected) in enumerate(test_cases, 1):
        output = solution.isAnagram(s, t)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")