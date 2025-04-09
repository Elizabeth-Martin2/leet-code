from collections import defaultdict

class Solution:
    """
    Given an array of integers (arr) and a target (k) return
    the number of pairs of array elements that have a difference
    equal to the target value.
    """

    # Analysis: time = O(n), space = O(n)
    # where n = len(arr)
    def pairs(self, k, arr):
        count = 0
        freq = defaultdict(int)
        new_arr = []

        for num in arr:
            freq[num] += 1
            new_arr.append(num - k)

        for num in new_arr:
            if num in freq:
                count += freq[num]

        return count


    # Brute force approach -- 13/18 test cases passed
    # Analysis: time = O(n^2), space = O(1)
    def pairsBF(self, k, arr):
        count = 0
        n = len(arr)

        for i in range(0, n):
            for j in range(0, n):
                if i == j:
                    continue

                if arr[j] - arr[i] == k:
                    count += 1

        return count


if __name__ == "__main__":
    soluion = Solution()
    test_cases = [
        (1, [1, 2, 3, 4], 3),
        (5, [1, 2, 3], 0),
        (100, [1, 101, 201], 2)
    ]

    for i, (target, nums, expected) in enumerate(test_cases, 1):
        output = soluion.pairs(target, nums)
        assert output == expected, f"Opt Test case {i} failed, expected {expected}, got {output}"

        output = soluion.pairsBF(target, nums)
        assert output == expected, f"BF Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")