class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return 0
        
        nums.sort()
        count = 0
        f_ptr = 0
        s_ptr = len(nums) - 1
        
        while f_ptr < s_ptr:
            current_sum = nums[f_ptr] + nums[s_ptr]
            if current_sum == k:
                count += 1
                f_ptr += 1
                s_ptr -= 1
            elif current_sum < k:
                f_ptr += 1
            else:
                s_ptr -= 1
            
        return count
