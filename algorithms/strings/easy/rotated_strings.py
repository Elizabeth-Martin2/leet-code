class Solution:
    """
    Given two strings (s, goal) determine if the second
    string can be achieved by rotating the first and return
    a boolean value accordingly.

    LC. 796 Rotate String
    """

    # Optimized Analysis: time = O(n), space = O(n)
    def rotateStringOpt(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s


    # Brute Force Analysis: time = O(n^2), space = O(1)
    # where n = len(goal)
    def rotateStringBF(self, s: str, goal: str) -> bool:
        s_len, g_len = len(s), len(goal)
        
        # Base cases
        if s_len != g_len:
            return False
        if s == goal:
            return True
        
        for i in range(0, g_len):
            if s[0] == goal[i]:
                temp = goal[i:] + goal[:i] # this creates a new string every time = O(n)

                if temp == s:
                    return True
            
        return False


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("abcde", "cdeab", True),
        ("abcde", "abced", False),
        ("aabaaba", "aaabaab", True)
    ]

    for i, (s, goal, expected) in enumerate(test_cases, 1):
        output = solution.rotateStringOpt(s, goal)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")