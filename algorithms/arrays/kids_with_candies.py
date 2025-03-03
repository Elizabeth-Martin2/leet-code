class Solution:
    """Determines which kids can have the most candies after adding extra candies."""

    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        res = []
        max_candies = max(candies)

        for candy in candies:
            res.append(candy + extraCandies >= max_candies)

        return res


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([2, 3, 5, 1, 3], 3, [True, True, True, False, True]),
        ([4, 2, 1, 1, 2], 1, [True, False, False, False, False]),
        ([12, 1, 12], 10, [True, False, True]),
        ([1, 1, 1, 1], 0, [True, True, True, True]),
    ]

    for i, (candies, extra, expected) in enumerate(test_cases, 1):
        assert solution.kidsWithCandies(candies, extra) == expected, f"Test case {i} failed"

    print("All test cases passed!")
