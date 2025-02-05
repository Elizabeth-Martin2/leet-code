class Solution:
    """Checks if an array is sorted and rotated"""

    # Attempt 2: Optimized version of check()
    # Analysis: O(n)
    def check_optimized(self, nums: list[int]) -> bool:
        n = len(nums)
        count_breaks = 0

        for i in range(n): # O(n)
            # Wrap around array to check for breaks
            if nums[i] > nums[(i + 1) % n]:
                count_breaks += 1
                if count_breaks > 1:
                    return False

        return True

    # Attempt 1: Same complexity as optimized, but slightly inefficient
    # Analysis: O(n)
    def check(self, nums: list[int]) -> bool:
        j = rotating_ind = -1
        n = len(nums)
        i = 0
        
        # Check for sorted & find rotating index
        while i in range(n) and rotating_ind == -1: # O(n)
            if nums[i] >= j:
                j = nums[i]
            else:
                rotating_ind = i
            i += 1

        if rotating_ind == -1:
            # Already sorted
            return True
        
        # Avoid creating new arrays to save space
        counter = 0
        i = rotating_ind
        j = -1

        while counter < n:
            # Use i to cycle through nums & reset at the end
            if i >= n:
                i = 0
            if nums[i] >= j:
                j = nums[i]
            else:
                return False
            i += 1
            counter += 1
        return True


if __name__ == "__main__":
    nums1 = [3,4,5,1,2]

    print(f"nums1: {nums1}; Sorted & rotated: {Solution().check_optimized(nums1)}")

    nums2 = [1,1,1]
    print(f"nums2: {nums2}; Sorted & rotated: {Solution().check_optimized(nums2)}")

    nums3 = [6,10,6]
    print(f"nums3: {nums3}; Sorted & rotated: {Solution().check_optimized(nums3)}")

    nums4 = [2,1,3,4]
    print(f"nums4: {nums4}; Sorted & rotated: {Solution().check_optimized(nums4)}")