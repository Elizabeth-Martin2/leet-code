class Solution:
    """
    Given two non-negative integers, num1 and num2 represented as string,
    return the sum of num1 and num2 as a string.

    Note: You must solve the problem without using any built-in library for
    handling large integers (such as BigInteger). You must also not convert
    the inputs to integers directly.

    LC. 415 Add Strings
    """

    # Analysis: time = O(n), space = O(n)
    # where n = max(len(num1), len(num2))
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        res = []

        while i >= 0 or j >= 0 or carry:
            n1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            n2 = ord(num2[j]) - ord('0') if j >= 0 else 0

            total = n1 + n2 + carry
            res.append(chr((total % 10) + ord('0'))) # get leading digit
            carry = total // 10 # get carry over amount

            i -= 1
            j -= 1

        return ''.join(reversed(res))
    

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("123", "12", "135"),
        ("99", "1", "100"),
        ("76", "4", "80")
    ]

    for i, (str1, str2, expected) in enumerate(test_cases, 1):
        output = solution.addStrings(str1, str2)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")