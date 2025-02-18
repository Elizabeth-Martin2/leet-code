class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Base case
        length = len(nums)
        if length < 3:
            return False

        small = med = float('inf')
        for num in nums:
            if num < small:
                small = num
            elif small < num < med:
                med = num
            elif num > med:
                return True

        return False