class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        i = len_nums - 2

        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1

        print(i, nums[i])
        if i >= 0:
        
            j = len_nums - 1
            while nums[j] <= nums[i]:
                j -= 1
            
            nums[j], nums[i] = nums[i], nums[j]

        nums[i + 1:] = reversed(nums[i + 1:])