class Solution:
    """Calculates the next lexicographically increasing permutation"""

    def next_permutation(self, nums: list[int]) -> None:
        """
        Updates the nums array in place to the next lexicographically increasing permutation.
        Generalized steps:
          1. Backtracking from the right side, find the pivot point where numbers decrease
          2. Find the smallest number larger than pivot on right side and swap with pivot
          3. Reverse everything after pivot index + 1 to get smallest next permutation
        """
        len_nums = len(nums)
        i = len_nums - 2

        # 1. Find the pivot
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1

        if i >= 0:
            # 2. Find smallest number larger than pivot on right
            j = len_nums - 1
            while nums[j] <= nums[i]:
                j -= 1
            # 2. (cont'd) swap with pivot
            nums[j], nums[i] = nums[i], nums[j]

        # 3. Reverse after pivot index + 1
        nums[i + 1:] = reversed(nums[i + 1:])

if __name__ == "__main__":
    solution = Solution()

    nums1 = [1,2,3]
    solution.next_permutation(nums1)
    assert nums1 == [1,3,2], "Test case 1 failed"

    nums2 = [3,2,1]
    solution.next_permutation(nums2)
    assert nums2 == [1,2,3], "Test case 2 failed"

    nums3 = [1,3,6,4,2,5]
    solution.next_permutation(nums3)
    assert nums3 == [1,3,6,4,5,2], "Test case 3 failed"

    print("All test cases passed!")