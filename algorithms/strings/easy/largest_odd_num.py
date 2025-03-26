class Solution:
    """
    Given a number as a string (num) return the largest
    odd number substring present in the string.

    LC. 1903 Largest Odd Number in a String
    """

    # Analysis: time = O(n), space = O(1)
    # where n = len(num)
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if num[i] in {"1", "3", "5", "7", "9"}:
                return num[:i + 1]      

        return ""


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        ("52", "5"),
        ("4206", ""),
        ("35427", "35427")
    ]

    for i, (num, expected) in enumerate(test_cases,1):
        output = s.largestOddNumber(num)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")