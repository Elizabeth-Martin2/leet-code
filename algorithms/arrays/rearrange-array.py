class Solution:
    """Rearrange an array of positive and negative integers"""

    # Analysis: time = O(n), space = O(n)
    # Note: While a O(1) space implementation is possible, it will increase the time to O(n^2) since
    # we must maintain the relative order of same signed numbers.
    def rearrange_array(self, nums: list[int]) -> list[int]:
        """
        Return a list of rearranged integers with the following constraints: 
          1. Every consecutive pair of integers have opposite signs
          2. For all integers with the same sign, the order in which they were present in nums is preserved
          3. The rearranged array begins with a positive integer
        """
        pos_nums = []
        neg_nums = []
        for num in nums:
            if num > 0:
                pos_nums.append(num)
            else:
                neg_nums.append(num)
        
        return [x for pair in zip(pos_nums, neg_nums) for x in pair]

if __name__ == "__main__":
    solution = Solution()

    nums1 = [3,1,-2,-5,2,-4]
    assert solution.rearrange_array(nums1) == [3,-2,1,-5,2,-4], "Test case 1 failed"

    nums2 = [-1,1]
    assert solution.rearrange_array(nums2) == [1,-1], "Test case 2 failed"

    nums3 = [-2,-6,3,4,-5,7]
    assert solution.rearrange_array(nums3) == [3,-2,4,-6,7,-5], "Test case 3 failed"

    print("All test cases passed!")