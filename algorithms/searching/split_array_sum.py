class Solution:
    """
    Given an array of integers (nums) split the integers into a
    given number (k) of groups such that the maximum sum of the
    groups is minimized.
    
    Uses binary search to find the minimized sum.
    LC. 410 Split Array Largest Sum
    """

    # Analysis: time = O(n log(sum(nums))), space = O(1)
    # where n = len(nums)
    def splitArray(self, nums: list[int], k: int) -> int:
        if k == len(nums):
            return max(nums)
        
        left, right = max(nums), sum(nums)

        # Function analysis: time = O(n), space = O(1)
        # where n = len(nums)
        def split_check(target:int) -> bool:
            current_sum = 0
            group_count = 1

            for num in nums:
                if current_sum + num <= target:
                    current_sum += num
                else:
                    current_sum = num
                    group_count += 1
                    if group_count > k:
                        return False
            
            return True

        while left < right:
            mid = (left + right) // 2
            
            if split_check(mid):
                right = mid
            else:
                left = mid + 1
            
        return left

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([7,2,5,10,8], 2, 18),
        ([1,2,3,4,5], 2, 9),
        ([1,4,4], 3, 4)
    ]

    for i, (nums, k, expected) in enumerate(test_cases, 1):
        output = solution.splitArray(nums, k)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")