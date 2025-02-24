class Solution:
    """Merge nums2 into nums1 in-place."""
    
    # Analysis: time = O(n), space = O(1)
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        ptr1, ptr2 = m-1, n-1
        i = len(nums1) - 1

        while ptr1 >= 0 and ptr2 >= 0:
            if nums1[ptr1] >= nums2[ptr2]:
                nums1[i] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[i] = nums2[ptr2]
                ptr2 -= 1
            
            i -= 1

        while ptr2 >= 0:
            nums1[i] = nums2[ptr2]
            i -= 1
            ptr2 -= 1


if __name__ == "__main__":
    test_cases = [
        # nums1, m, nums2, n, expected
        ([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1])
    ]

    solution = Solution()
    for i, (nums1, m, nums2, n, expected) in enumerate(test_cases):
        solution.merge(nums1, m, nums2, n)
        assert nums1 == expected, f"Test case {i} failed: expected {expected} got {nums1}"
        print(f"Test case {i} passed!")

    print("All test cases passed!")