class Solution:
    """Finds all leaders in an array."""

    # Analysis: time = O(n), space = O(n)
    def leaders(self, arr: list[int]) -> list[int]:
        i = len(arr) - 1
        current_max = -1
        sol = []

        while i >= 0:
            if arr[i] >= current_max:
                sol.append(arr[i])
                current_max = arr[i]
            i -= 1

        return list(reversed(sol))


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 3, 9, 2, 7, 4, 1], [9, 7, 4, 1]),
        ([16, 17, 4, 3, 5, 2], [17, 5, 2]),
        ([30, 10, 10, 5], [30, 10, 10, 5]),
        ([1, 2, 3, 4, 5], [5]),
    ]

    for i, (arr, expected) in enumerate(test_cases, 1):
        assert solution.leaders(arr) == expected, f"Test case {i} failed"

    print("All test cases passed!")
