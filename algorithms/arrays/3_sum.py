class Solution:
    """Returns lists of distinct integers that sum to zero"""

    # Analysis: time = O(n^2), space = O()
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i -1]:
                continue # Skip this iteration 
            
            left = i + 1 
            right = len(nums) - 1
            
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else: # == 0
                    res.append([nums[i], nums[left], nums[right]])

                    # Avoid duplicate values
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return res


if __name__ == "__main__":
    solution = Solution()
    nums1 = [-1,0,1,2,-1,-4]
    res1 = [[-1,-1,2],[-1,0,1]]

    nums2 = [0,1,1]
    res2 = []

    nums3 = [-2,0,0,2,2]
    res3 = [[-2,0,2]]

    test_cases = [nums1, nums2, nums3]
    test_case_ress = [res1, res2, res3]

    for i, test in enumerate(test_cases):
        assert solution.threeSum(test) == test_case_ress[i], f"Test case {i} failed"

    print("All test cases passed!")