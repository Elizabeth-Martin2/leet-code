class Solution:
    """Finds the single number in an array"""

    # Analysis: time = O(n), space = O(1)
    def single_number(self, nums: list[int]) -> int:
        """Returns the single number in a given array"""
        result = 0
        for num in nums:
            result ^= num
        return result


if __name__ == "__main__":
    nums1 = [4,1,2,1,2]
    print(f"Nums1: {nums1}, single number: {Solution().single_number(nums1)}")

    nums2 = [2,2,1]
    print(f"Nums2: {nums2}, single number: {Solution().single_number(nums2)}")

    nums3 = [1]
    print(f"Nums3: {nums3}, single number: {Solution().single_number(nums3)}")