class Solution:
    """
    Find the maximum distance a given number of cows can be placed
    in the given number of stalls.

    Uses binary search to find the maximum distance.
    """

    # Analysis: time = O(m log n), space = O(1)
    # where n = max(stalls), m = number of stalls
    def preventAggrocows(self, cows:int, stalls:list[int]) -> int:
        left, right = 1, max(stalls)
        stalls.sort()

        while left <= right:
            distance = (left + right) // 2
            cow_count, last_cow = cows - 1, stalls[0]

            for i in range(1, len(stalls)):
                if stalls[i] >= last_cow + distance:
                    last_cow = stalls[i]
                    cow_count -= 1

            if cow_count > 0:
                right = distance - 1
            else:
                left = distance + 1

        return right


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (3, [1,2,8,4,9], 3),
        (2, [10, 20, 30, 40, 50], 40),
        (4, [1, 3, 6, 10, 15], 4)
    ]

    for i, (cows, stalls, expected) in enumerate(test_cases, 1):
        output = solution.preventAggrocows(cows, stalls)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")
