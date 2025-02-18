class Solution:
    """Finds the maximum number of consecutive ones"""

    # Analysis: time = O(n), space = O(1)
    def find_max_consecutive_ones(self, nums: list[int]) -> int:
        """Returns the maximum number of consecutive ones in a binary array"""
        max_count = current_count = 0
        for num in nums:
            if num == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
        return max_count

if __name__ == "__main__":
    nums1 = [1,1,0,1,1,1]
    print(f"Nums1: {nums1}, max consecutive ones: {Solution().find_max_consecutive_ones(nums1)}")

    nums2 = [1,0,1,1,0,1]
    print(f"Nums2: {nums2}, max consecutive ones: {Solution().find_max_consecutive_ones(nums2)}")