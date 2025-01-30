import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prods = [1] * n
        sol = [1] * n

        # Demo input: nums = [1, 2, 3, 4]
        # Create prefix prod array ; e.g., [1, 1, 2, 6]
        for i in range(1, n):
            prefix_prods[i] = prefix_prods[i-1] * nums[i-1]

        # range(start, stop, step)
        suffix_prod = 1
        for i in range(n - 1, -1, -1):
            sol[i] = prefix_prods[i] * suffix_prod
            suffix_prod *= nums[i]

        return sol
