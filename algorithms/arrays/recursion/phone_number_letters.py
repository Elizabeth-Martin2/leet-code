class Solution:
    """
    Given a string representing a list of digits, return all possible letter combinations
    those digits could create when texting on an *old* phone.

    Example:
        Input: digits = "23"
        Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

    LC. 17 Letter Combinations of a Phone Number
    """

    # Analysis: time = O(4^n), space = O(n)
    # where n = length of digits
    def letterCombinations(self, digits: str) -> list[str]:
        number_to_letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        len_digits = len(digits)

        def helper(current: list[str] = [], ind: int = 0) -> None:
            if ind == len_digits:
                res.append("".join(current[:]))
                return

            letters = number_to_letter.get(digits[ind])
            for letter in letters:
                # Choice 1: Take the current letter & move to next digit
                current.append(letter)
                helper(current, ind + 1)
                
                # Choice 2: Skip the current letter
                current.pop()

        if digits != "":
            helper()
        return sorted(res)


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
        ("2", ["a","b","c"]),
        ("", [])
    ]

    for i, (digits, expected) in enumerate(test_cases, 1):
        output = s.letterCombinations(digits)
        assert output == expected, f"Optimized Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")
