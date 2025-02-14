class Solution:
    """
    Finds the leaders in an array of integers.

    Leader definition: An element is considered a leader if it is
    greater than or equal to all elements to its right.
    """

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

    nums1 = [1, 3, 9, 2, 7, 4, 1]
    assert solution.leaders(nums1) == [9, 7, 4, 1], "Test case 1 failed"

    nums2 = [16, 17, 4, 3, 5, 2]
    assert solution.leaders(nums2) == [17, 5, 2], "Test case 2 failed"

    nums3 = [30, 10, 10, 5]
    assert solution.leaders(nums3) == [30, 10, 10, 5], "Test case 3 failed"

    print("All test cases passed!")
