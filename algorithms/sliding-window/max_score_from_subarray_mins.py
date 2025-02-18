class Solution:
    """Finds the maximum score using minimum values in subarrays"""

    # Analysis: time = O(n), space = O(1)
    def pair_with_max_sums(self, arr: list[int]) -> int:
        """Return the maximum score of the minimum integers in any subarray"""

        n = len(arr)
        if n < 2:
            raise ValueError("Array must have at least 2 elements")
        
        m_s = arr[0] + arr[1]
        
        for i in range(1, n - 1):
            min1 = min(arr[i], arr[i + 1])
            min2 = max(arr[i], arr[i + 1])
            m_s = max(m_s, min1 + min2)
        
        return m_s

if __name__ == "__main__":
    solution = Solution()

    nums1 = [4, 3, 1, 5, 6]
    assert solution.pair_with_max_sums(nums1) == 11, "Test case 1 failed"

    nums2 = [228, 394, 463, 227, 388, 757, 782, 238, 967]
    assert solution.pair_with_max_sums(nums2) == 1539, "Test case 2 failed"

    print("All test cases passed!")