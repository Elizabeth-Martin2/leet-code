class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Use sliding window approach
        
        # Base case
        if k >= len(nums):
            return sum(nums[0:]) / k

        # Can't initialize max_average to 0
        max_sum = sum(nums[0:k])
        next_sum = max_sum
        for i in range(k, len(nums)):
            next_sum += nums[i] - nums[i-k]
            max_sum = max(next_sum, max_sum)

        return max_sum / k