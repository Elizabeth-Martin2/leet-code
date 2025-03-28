class Solution:
    """
    Given a binary array (nums) and an integer (k), return the
    maximum number of consecutive 1's in the array if you can
    flip at most k 0's.

    LC. 1004 Max Consecutive Ones 3
    """

    # Analysis: time = O(n), space = O(1)
    def longestOnes(self, nums: list[int], k: int) -> int:
        start, max_len = 0, 0
        o_count = 0

        for end in range(len(nums)):
            if nums[end] == 0 and o_count <= k:
                o_count += 1

            while o_count > k:
                if nums[start] == 0:
                    o_count -= 1
                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1,1,1,0,0,0,1,1,1,1,0], 2, 6),
        ([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3, 10),
        ([1,0,0,1,1,0,1,1,1], 2, 7)
    ]

    for i, (nums, k, expected) in enumerate(test_cases, 1):
        output = solution.longestOnes(nums, k)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")
