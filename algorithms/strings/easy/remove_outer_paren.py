class Solution:
    """
    Remove outer parentheses of every primitive string in a given string (s).

    LC. 1021 Remove Outermost Parentheses
    """
    
    # Analysis: time = O(n), space = O(n)
    # where n = len(s)
    def removeOuterParentheses(self, s: str) -> str:
        if not s:
            return ""
        
        res = []
        start, count = 0, 0
        
        for i, letter in enumerate(s):            
            if letter == "(":
                count += 1
            elif letter == ")":
                count -= 1

            if count == 0:
                res.append(s[start + 1:i])
                start = i + 1

        return "".join(res)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("(()())(())", "()()()"),
        ("(()())(())(()(()))", "()()()()(())"),
        ("()()", "")
    ]

    for i, (test_string, expected) in enumerate(test_cases, 1):
        output = solution.removeOuterParentheses(test_string)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")