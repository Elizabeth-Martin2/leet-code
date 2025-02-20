class Solution:
    """Returns distinct lists of integers summing to an input target."""

    # Analysis: time = O(n^3), space = O(1)
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        
        # Base cases -- early quitting
        if n < 4:
            return []
        elif n == 4:
            return [nums] if sum(nums) == target else []
        
        res = []
        nums.sort()

        for i in range(len(nums)): 
            if i > 0 and nums[i] == nums[i - 1]:
                continue # skip this iteration

            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue # skip this iteration
                left = j + 1
                right = len(nums) - 1
                
                while left < right:
                    quad = nums[i] + nums[j] + nums[left] + nums[right]
                    if quad < target:
                        left += 1
                    elif quad > target:
                        right -= 1
                    else: # quad == target                       
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Avoid duplicate quadrupltes
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1
        
        return res


if __name__ == "__main__":
    solution = Solution()

    nums1 = [1,0,-1,0,-2,2]
    target1 = 0
    res1 = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

    nums2 = [2,2,2,2,2]
    target2 = 8
    res2 = [[2,2,2,2]]

    nums3 = [-1,0,-1,0,-2,-2]
    target3 = 0
    res3 = []

    nums4 = [-2,-1,-1,1,1,2,2]
    target4 = 0
    res4 = [[-2,-1,1,2],[-1,-1,1,1]]

    test_cases = [nums1, nums2, nums3, nums4]
    targets = [0 , 8, 0, 0]
    ress = [res1, res2, res3, res4]

    for i, test in enumerate(test_cases):
        assert solution.fourSum(test, targets[i]) == ress[i], f"Test case {i + 1} failed"

    print("All test cases passed!")







