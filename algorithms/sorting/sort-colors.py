class Solution:
    """Sorts an array of colors"""
    
    # Analysis: time = O(n), space = O(1)
    def sort_colors(self, nums: list[int]) -> None:
        """
        Sorts an array of colors represented by integers in place using the Dutch National Flag Algorithm.
        """
        r = -1
        b = len(nums) - 1
        i = 0

        while i <= b:
            if nums[i] == 0:
                r += 1
                nums[i], nums[r] = nums[r], nums[i]
                i += 1
            elif nums[i] == 2:
                nums[i], nums[b] = nums[b], nums[i]
                b -= 1
            else:
                i += 1
                
            
if __name__ == "__main__":
    solution = Solution()
    nums1 = [2,0,2,1,1,0]
    solution.sort_colors(nums1)
    assert nums1 == [0,0,1,1,2,2], "Test case 1 failed"

    nums2 = [2,0,1]
    solution.sort_colors(nums2)
    assert nums2 == [0,1,2], "Test case 2 failed"

    print("All test cases passed!")
