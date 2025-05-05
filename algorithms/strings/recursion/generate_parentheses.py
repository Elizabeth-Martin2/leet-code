class Solution:
    """
    Given n pairs of parentheses, write a function to generate all
    combinations of well-formed parentheses.

    LC. 22 Generate Parentheses
    """
    DEBUG = False

    @staticmethod
    def _debug(*args, **kwargs):
        if Solution.DEBUG:
            print(*args, **kwargs)

    # Analysis: time = O(n), space = O(n) [due to recursive call stack]
    def generateParenthesis(self, n: int) -> list[str]:
        def _backtrack(n:int, opens:int, closes:int, current:str, res:list[str]):
            if len(current) == n * 2:
                Solution._debug("(Long enough) current:", current)
                Solution._debug("---------------------")
                res.append(current)
                return

            Solution._debug("(Too short) current:", current)
            if opens < n:
                _backtrack(n, opens + 1, closes, current + '(', res)

            if closes < opens:
                _backtrack(n, opens, closes + 1, current + ')', res)

        res = []
        _backtrack(n, 0, 0, "", res)
        return res


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        (3, ["((()))","(()())","(())()","()(())","()()()"]),
        (1, ["()"]),
        (2, ['(())', '()()'])
    ]

    for i, (n, expected) in enumerate(test_cases, 1):
        output = s.generateParenthesis(n)
        assert sorted(output) == sorted(expected), f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")