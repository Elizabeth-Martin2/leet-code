class Solution:
    """
    Use a stack to validate if parentheses pairs are correct.
    LC. 20 Valid Parentheses
    """

    # Analysis: time = O(n), space = O(n)
    # where n = len(s)
    def isValid(self, s: str) -> bool:
        stack = []

        for paren in s:
            if not stack:
                stack.append(paren)
            
            elif paren == ")" and stack[-1] == "(":
                stack.pop()
            elif paren == "}" and stack[-1] == "{":
                stack.pop()
            elif paren == "]" and stack[-1] == "[":
                stack.pop()
            
            else:
                stack.append(paren)
        
        return len(stack) == 0

if __name__ == "__main__":
    soluion = Solution()
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False)
    ]

    for i, (parens, expected) in enumerate(test_cases, 1):
        output = soluion.isValid(parens)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")