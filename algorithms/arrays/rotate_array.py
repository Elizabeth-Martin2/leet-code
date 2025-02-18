class Solution:
    """Class to perform in-place array rotation"""

    def reverse(self, nums:list[int], left: int, right:int):
        """Reverses integers between left & right positions"""
        while left < right: # O(right - left)
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    # Analysis: time = O(n) ; space = O(1)
    def rotate(self, nums: list[int], k: int) -> None:
        """Rotates an array k positions to the right in-place"""
        n = len(nums)
        if not nums or len(nums) == 1:
            return

        k = k % n # for cases where k > n
        self.reverse(nums, 0, n - 1) # O(n)
        self.reverse(nums, 0, k - 1) # O(k)
        self.reverse(nums, k, n - 1) # O(n - k)

if __name__ == "__main__":
    nums1 = [1,2,3,4,5,6,7]
    print(f"Nums1: {nums1}")
    Solution().rotate(nums1, 3)
    print(f"Rotated 3 positions: {nums1}")

    nums2 = [1,2]
    print(f"Nums2: {nums2}")
    Solution().rotate(nums2, 3)
    print(f"Rotated 3 positions: {nums2}")

    nums3 = [-1]
    print(f"Nums3: {nums3}")
    Solution().rotate(nums3, 2)
    print(f"Rotated 2 positions: {nums3}")



# # Brute force - attempt 1
# # Analysis: time = O(n) ; space = O(n)
# def brute_force_rotate(self, nums: list[int], k: int) -> None:
#     if nums == None or len(nums) == 1:
#         return

#     n = len(nums)
#     rotated_nums = [-1] * n
#     for i in range(n): # O(n)
#         new_pos = (i + k) % n
#         rotated_nums[new_pos] = nums[i]

#     print(rotated_nums)
#     for i in range(n): # O(n)
#         nums[i] = rotated_nums[i]
