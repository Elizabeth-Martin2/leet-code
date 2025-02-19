import math
class Solution:
    """Finds the majority element in an array"""

    # Analysis: time = O(n), space = O(1)
    def majority_element_half(self, nums: list[int]) -> int:
        """
        Returns the majority integer in an array using the Boyer-Moore Voting Algorithm where
        the majority integer occurs repeatedly for more than half of the integers of the input.

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

    # Analysis: time = O(n), space = O(1)
    def majority_element_third(self, nums: list[int]) -> list[int]:
        """
        Returns the majority integer in an array using the Boyer-Moore Voting Algorithm where
        the majority integer occurs repeatedly for more than a third of the integers of the input.
        """

        candidate1, candidate2, = None, None
        count1, count2 = 0, 0

        # Find potential candidates
        for num in nums: # O(n) time
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # Verify candidates' majority
        count1, count2 = 0,0
        for num in nums: # O(n) time
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        res = []
        maj = math.floor(len(nums) / 3)
        if count1 > maj:
            res.append(candidate1)
        if count2 > maj:
            res.append(candidate2)

        return res

if __name__ == "__main__":
    solution = Solution()

    nums1 = [3,2,3]
    assert solution.majority_element_half(nums1) == 3, "Test case 1 failed"
    assert solution.majority_element_third(nums1) == [3], "Test case 2 failed"

    nums2 = [2,2,1,1,1,2,2]
    assert solution.majority_element_half(nums2) == 2, "Test case 3 failed"
    assert solution.majority_element_third(nums2) == [2,1], "Test case 4 failed"

    nums3 = [1]
    assert solution.majority_element_half(nums3) == 1, "Test case 5 failed"
    assert solution.majority_element_third(nums3) == [1], "Test case 6 failed"

    nums4 = [1,2]
    # This test case doesn't follow the guarantee provided for majority_element_half
    assert solution.majority_element_third(nums4) == [1,2], "Test case 7 failed"

    print("All test cases passed!")