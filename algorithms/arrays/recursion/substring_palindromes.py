class Solution:
    """
    Given a string s, partition s such that every substring 
    of the partition is a palindrome. Return all possible 
    palindrome partitioning of s.

    LC. 131 Palindrome Partitioning
    """

    DEBUG = False

    @staticmethod
    def _debug(*args, **kwargs):
        if Solution.DEBUG:
            print(*args, **kwargs)

    # Helper function to check if a substring is a palindrome
    # Analysis: time = O(n), space = O(1)
    @staticmethod
    def is_palindrome(s:str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True

    # Analysis: time = O(n * 2^n), space = O(2^n * n) [due to the output]
    def partition(self, s: str) -> list[list[str]]:
        res = []
        len_s = len(s)

        def backtrack(start: int, path: list[str]) -> None:
            Solution._debug(f"start: {start}, path: {path}")
            if start == len_s:
                res.append(path[:])
                return
            
            for end in range(start + 1, len_s + 1):
                prefix = s[start:end]
                Solution._debug(f"prefix: {prefix}")
                if Solution.is_palindrome(prefix):
                    path.append(prefix)
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return res


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        ("aab", [["a","a","b"],["aa","b"]]),
        ("a", [["a"]]),
        ("aba", [["a","b","a"],["aba"]])
    ]

    for i, (letters, expected) in enumerate(test_cases, 1):
        output = s.partition(letters)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")