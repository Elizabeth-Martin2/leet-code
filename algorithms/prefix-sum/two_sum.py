class Solution:
    """Find two integers that add up to the target sum"""

    # Analysis: time = O(n), space = O(n) 
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Returns a list of two indices that add up to the target sum.

        Assumptions provided: each input has exactly one solution,
        and elements may be used only once
        """
        prefix_sum = {} # O(n) space

        for i, num in enumerate(nums): # O(n) time
            solution = target - num
            if solution in prefix_sum:
                if prefix_sum[solution] != i:
                    return i, prefix_sum[solution]
            
            prefix_sum[num] = i

        return [-1, -1] # Should never be reached, but included for completion

if __name__ == "__main__":
    solution = Solution()

    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    assert nums1[result1[0]] + nums1[result1[1]] == target1, "Test Case 1 Failed"

    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    assert nums2[result2[0]] + nums2[result2[1]] == target2, "Test Case 2 Failed"

    nums3 = [3, 3]
    target3 = 6
    result3 = solution.twoSum(nums3, target3)
    assert nums3[result3[0]] + nums3[result3[1]] == target3, "Test Case 3 Failed"

    print("All test cases passed!")