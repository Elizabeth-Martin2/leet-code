class Solution:
    """Moves unique integers to front of array and returns num of unique integers in the array"""

    # Analysis: O(n)
    def remove_duplicates(self, nums: list[int]) -> int:
        if not nums: # Base case
            return 0

        unique_ind = 1 # Slow pointer
        for fast in range(1, len(nums)):
            if nums[fast] != nums[unique_ind - 1]:
                nums[unique_ind] = nums[fast]
                unique_ind += 1
        
        return unique_ind

if __name__ == "__main__":
    nums1 = [1,1,2]
    print(f"Nums1: {nums1}")
    unique_nums1 = Solution().remove_duplicates(nums1)
    print(f"Unique numbers ({unique_nums1}): {nums1[:unique_nums1]}")

    print("---------------------------")

    nums2 = [0,0,1,1,1,2,2,3,3,4]
    print(f"Nums2: {nums2}")
    unique_nums2 = Solution().remove_duplicates(nums2)
    print(f"Unique numbers ({unique_nums2}): {nums2[:unique_nums2]}")