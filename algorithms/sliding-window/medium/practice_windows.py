class Solution: 
    """
    Given an array nums and an integer k, return the maximum sum of any subarray of size k.

    Example:
        nums = [2, 1, 5, 1, 3, 2], k = 3
        Output: 9  # because [5, 1, 3] has the largest sum = 9

    """

    def setWindow(self, nums: list[int], k: int) -> int:
        max_sum, window_sum = 0, 0
        start = 0

        if len(nums) <= k:
            return sum(nums)
        
        window_sum = sum(nums[:k])
        max_sum = window_sum
        print(f"first window sum: {max_sum}")

        for end in range(k, len(nums)):
            window_sum = window_sum - nums[start] + nums[end]
            print(f"next window sum: {window_sum}")

            max_sum = max(max_sum, window_sum)

            start += 1

        return max_sum


    def variableWindow(self, nums: list[int], k:int) -> int:
        """
        Given an array nums of non-negative integers and an integer k,
        return the length of the longest subarray such that the sum of its elements is less than or equal to k.

        Example:
            nums = [1, 2, 1, 0, 1, 1, 0], k = 4
            Output: 5
            # The subarray [1, 2, 1, 0] has sum 4 and length 4
            # The subarray [2, 1, 0, 1] has sum 4 and length 4
            # The subarray [1, 0, 1, 1, 0] has sum 3 and length 5 → ✅ longest
        """

        start, curr_sum, max_len = 0, 0, 0

        for end in range(len(nums)):
            curr_sum += nums[end]

            while curr_sum > k:
                curr_sum -= nums[start]
                start += 1

            max_len = max(end - start + 1, max_len)

        return max_len



if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1, 2, 1, 0, 1, 1, 0], 4, 5)
    ]

    for i, (nums, k, expected) in enumerate(test_cases, 1):
        output = solution.variableWindow(nums, k)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")