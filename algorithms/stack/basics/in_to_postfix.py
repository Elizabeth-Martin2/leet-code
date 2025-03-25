class Solution:
    """
    Given a string infix expression (s), return the postfix expression.

    Note: The order of precedence is: ^ greater than * equals to / greater
    than + equals to -. Ignore the right associativity of ^.
    """

    # Analysis: time = O(n), space = O(n)
    # where n = len(s)
    def InfixtoPostfix(self, s: str) -> str:
        op_stack = []
        res = []
        operators = {"^": 3, "*": 2, "/": 2, "+": 1, "-": 1}

        for ch in s:
            if ch.isalnum():
                res.append(ch)

            elif ch == "(":
                op_stack.append(ch)
            elif ch == ")":
                while op_stack and op_stack[-1] != "(":
                    res.append(op_stack.pop())

                op_stack.pop() # pop final "("

            else:
                prec = operators[ch]

                while op_stack and op_stack[-1] != "(" and operators[op_stack[-1]] >= prec:
                    res.append(op_stack.pop())
                    # print(f"Added {val} to res")
                op_stack.append(ch)

        while op_stack:
            res.append(op_stack.pop())

        return ''.join(res)


if __name__ == "__main__":    
    solution = Solution()

    test_cases = [
        ("a+b*(c^d-e)^(f+g*h)-i", "abcd^e-fgh*+^*+i-"),
        ("a+b*c", "abc*+"),
        ("(a+b)*c", "ab+c*"),
        ("a+b+c", "ab+c+"),
        ("a*(b+c)/d", "abc+*d/"),
        ("a+b*(c+d)", "abcd+*+"),
        ("a^b^c", "ab^c^"),
        ("(a+b)*(c+d)", "ab+cd+*"),
        ("a+b*(c^d)", "abcd^*+"),
    ]

    for i, (expr, expected) in enumerate(test_cases, 1):
        output = solution.InfixtoPostfix(expr)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")