class Solution:
    """
    Given an array of strictly increasing positive integers (arr)
    return the kth missing integer (k).

    Uses binary search to find the missing integer.

    LC. 1539: Kth Missing Positive Number
    """

    # Analysis: time = O(log n), space = O(1)
    # where n = len(arr)
    def findKthPositive(self, arr: list[int], k: int) -> int:
        left, right = 0, len(arr)
        count = 0

        while left < right:
            mid = (left + right) // 2

            count = arr[mid] - mid - 1

            if count < k: 
                left = mid + 1
            else:
                right = mid
        
        return left + k


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([2,3,4,7,11], 5, 9),
        ([4,5,6,7,8,9], 3, 3),
        ([1,2,3,4], 2, 6)
    ]

    for i, (arr, k, expected) in enumerate(test_cases, 1):
        output = solution.findKthPositive(arr, k)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")