class Solution:
    """Finds the majority element in an array"""

    def majority_element(self, nums: list[int]) -> int:
        """
        Returns the majority integer in an array using the Boyer-Moore Voting Algorithm

        Guarantees: There will always be a majority integer
        """

        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate

if __name__ == "__main__":
    solution = Solution()

    nums1 = [3,2,3]
    majority1 = solution.majority_element(nums1)
    assert majority1 == 3, "Test case 1 failed"

    nums2 = [2,2,1,1,1,2,2]
    majority2 = solution.majority_element(nums2)
    assert majority2 == 2, "Test case 2 failed"

    nums3 = [1]
    majority3 = solution.majority_element(nums3)
    assert majority3 == 1, "Test case 3 failed"

    print("All test cases passed!")