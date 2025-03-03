class Solution:
    """
    Determines if `n` new flowers can be planted in a flowerbed without violating the
    rule that no two flowers can be adjacent. Returns True if possible, otherwise False.
    """

    # Analysis: time = O(n), space = O(1)
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True

        for i in range(len(flowerbed)):
            if (
                flowerbed[i] == 0
                and (i == 0 or flowerbed[i - 1] == 0)
                and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            ):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True  # Early exit

        return n <= 0


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1, 0, 0, 0, 1], 1, True),
        ([1, 0, 0, 0, 1], 2, False),
        ([0], 1, True)
    ]

    for i, (flowerbed, n, expected) in enumerate(test_cases, 1):
        output = solution.canPlaceFlowers(flowerbed, n)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")
