class Solution:
    """Find the missing number in an array of n distinct numbers"""

    # Optimized
    # Analysis: time = O(n), space = O(1)
    def missing_number(self, nums: list[int]) -> int:
        """Returns the missing number from an array of n distinct numbers"""
        n = len(nums)
        expected_sum = n * (n + 1) // 2 # Gauss' formula for sum 0 to n
        actual_sum = sum(nums)
        return expected_sum - actual_sum
    
    
    # Brute force
    # Analysis: time = O(n), space = O(n)
    # def missing_number(self, nums: list[int]) -> int:
    #     n = len(nums)
    #     unique_nums = {}
    #     for num in nums:
    #         unique_nums[num] = 1

    #     for i in range(0, n+1):
    #         if i not in unique_nums:
    #             return i

    #     return -1 # Shouldn't ever happen, but included for completion


if __name__ == "__main__":
    nums1 = [3,0,1]
    print(f"Nums1: {nums1}, missing num: {Solution().missing_number(nums1)}")

    nums2 = [0,1]
    print(f"Nums2: {nums2}, missing num: {Solution().missing_number(nums2)}")

    nums3 = [9,6,4,2,3,5,7,0,1]
    print(f"Nums3: {nums3}, missing num: {Solution().missing_number(nums3)}")