from collections import deque
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

    # Analysis: time = O(n), space = O(n)
    # where n = len(s)
    def isBalanced(s):
        """
        This is another implementation from revisiting the question.
        It solves the same problem as above, but was required to return
        "YES" or "NO" as the result.
        """

        my_stack = deque()
        opens = {"{": 0, "(": 1, "[": 2}
        closes = {"}": 0, ")": 1, "]": 2}

        for i in range(len(s)):
            p = s[i]

            if p in opens:
                my_stack.append(p)
            elif p in closes:
                if not my_stack:
                    return "NO"

                last_p = my_stack.pop()
                if closes[p] != opens[last_p]:
                    return "NO"
            else:
                return "NO"

        if len(my_stack) > 0:
            return "NO"

        return "YES"


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