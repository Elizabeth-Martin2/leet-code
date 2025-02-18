class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two-pointer approach
        left_ptr = 0
        right_ptr = len(height) -1
        max_water = 0

        while left_ptr < right_ptr:
            # Calculate area
            area = min(height[left_ptr], height[right_ptr]) * (right_ptr - left_ptr)
            max_water = max(max_water, area)
            
            if height[left_ptr] < height[right_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1

        return max_water
