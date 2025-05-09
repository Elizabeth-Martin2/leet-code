class Solution:
    """
    Given an array nums of n integers, return the sums of all subsets of the array nums.

    Example:
        Input : nums = [2, 3]
        Output : [0, 2, 3, 5]

        Explanation:
        When no elements is taken then Sum = 0.
        When only 2 is taken then Sum = 2.
        When only 3 is taken then Sum = 3.
        When element 2 and 3 are taken then sum = 2+3 = 5.
    """

    DEBUG = False

    @staticmethod
    def _debug(*args, **kwargs):
        if Solution.DEBUG:
            print(*args, **kwargs)

    # Analysis: time = O(2^n), space = O(n)
    # where n = length of nums
    def subsetSums(self, nums: list[int]) -> list[int]:
        res = []
        nums_len = len(nums)
        Solution._debug(f"Starting nums: {nums}")

        def helper(current_sum: int = 0, index: int = 0) -> None:
            if index == nums_len:
                res.append(current_sum)
                Solution._debug(f"Adding {current_sum} to res")
                Solution._debug("--------------------------")
                return

            # Choice 1: Add num
            Solution._debug(f"({index}) Adding num: {nums[index]}, current_sum = {current_sum}")
            helper(current_sum + nums[index], index + 1)
            # Choice 2: Skip num
            Solution._debug(f"({index}) Skipping num: {nums[index]}, current_sum = {current_sum}")
            helper(current_sum, index + 1)

        helper()
        return sorted(res)


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        ([2,3], [0,2,3,5]),
        ([5,2,1], [0,1,2,3,5,6,7,8]),
        ([1,2,3,4], [0,1,2,3,3,4,4,5,5,6,6,7,7,8,9,10])
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        output = s.subsetSums(nums)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")
