class Solution:
    """
    Given a number n, generate all possible binary strings of length n.
    """
    DEBUG = False

    @staticmethod
    def _debug(*args, **kwargs):
        if Solution.DEBUG:
            print(*args, **kwargs)

    # Analysis: time = O(2^n), space = O(2^n) [for storing res]
    def generateBinaryStrings(self, n:int) -> list[str]:
        def _backtrack(n:int, res:list[str], current:str) -> None:
            if len(current) == n:
                res.append(current)
                Solution._debug("(Long enough) current:", current)
                Solution._debug("----------------------")
                return

            Solution._debug("(Too short) current:", current)
            _backtrack(n, res, current + "0")
            _backtrack(n, res, current + "1")

        res = []
        _backtrack(n, res, "")
        return res


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        (1, ['0', '1']),
        (2, ['00', '01', '10', '11']),
        (3, ['000', '001', '010', '011', '100', '101', '110', '111'])
    ]

    for i, (n, expected) in enumerate(test_cases, 1):
        output = s.generateBinaryStrings(n)
        assert sorted(output) == sorted(expected), f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")