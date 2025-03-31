from collections import deque

class Solution:
    """
    Given an array of integers nums and an integer limit, return the 
    size of the longest non-empty subarray such that the absolute 
    difference between any two elements of this subarray is less than
    or equal to limit.

    LC. 1438 1438. Longest Continuous Subarray With Absolute Diff Less 
    Than or Equal to Limit
    """

    # Analysis: time = O(n), space = O(n)
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        start, res = 0, 0
        max_d, min_d = deque(), deque()

        for end in range(len(nums)):
            # Maintain max & min of current window for abs val calcs
            while max_d and nums[end] > max_d[-1]:
                temp = max_d.pop()
            while min_d and nums[end] < min_d[-1]:
                temp = min_d.pop()
            
            max_d.append(nums[end])
            min_d.append(nums[end])

            # if the limit of the max & min of the windows is reached,
            # pop the start from the appropriate stack
            while max_d[0] - min_d[0] > limit:
                if nums[start] == max_d[0]:
                    temp = max_d.popleft()
                if nums[start] == min_d[0]:
                    temp = min_d.popleft()
                start += 1                

            res = max(res, end - start + 1)

        return res

        
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([8,2,4,7], 4, 2),
        ([10,1,2,4,7,2], 5, 4),
        ([4,2,2,2,4,4,2,2], 0, 3)
    ]

    for i, (nums, k, expected) in enumerate(test_cases, 1):
        output = solution.longestSubarray(nums, k)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")