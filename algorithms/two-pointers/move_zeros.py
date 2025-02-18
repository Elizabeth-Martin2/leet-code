class Solution:
    """Moves zeroes to the end of the array in-place"""

    # Analysis: time = O(n), space = O(1)
    def move_zeroes(self, nums: list[int]) -> None:
        """Moves all zeroes to the end of the array while maintaining relative order"""

        n = len(nums)
        fast = slow = 0
        while fast < n: # O(n)
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1

if __name__ == "__main__":
    nums1 = [0,1,0,3,12]
    print(f"Nums1: {nums1}")
    Solution().move_zeroes(nums1)
    print(f"Moved zeroes to end: {nums1}")

    nums2 = [0]
    print(f"Nums2: {nums2}")
    Solution().move_zeroes(nums2)
    print(f"Moved zeroes to end: {nums2}")