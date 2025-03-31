class Solution:
    def expand(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1:right]


    def longestPalindrome(self, s: str) -> str:
        res = ""
        
        for i in range(len(s)):
            temp = self.expand(s, i, i)
            if len(temp) > len(res):
                res = temp
            
            temp = self.expand(s, i, i + 1)
            if len(temp) > len(res):
                res = temp

        return res


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("babad", ["aba", "bab"]),
        ("cbbd", "bb"),
        ("hello", "ll")
    ]

    for i, (s, expected) in enumerate(test_cases, 1):
        output = solution.longestPalindrome(s)
        assert output in expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")
