class Solution:
    """
    Given an integer array nums representing the amount of money of each house, and
    the knowledge that robbing two houses in a row will alert the police, return the
    maximum amount of money you can rob tonight without alerting the police.

    Additionally, the houses on this street are arranged in a circle, so stealing from
    the first and last house will alert the police.

    LC. 213 House Robber 2
    """

    # Heler function analysis: time = O(n), space = O(1)
    # where n = number of houses
    def rob_houses(self, nums: list[int]) -> int:
        rob, skip = 0, 0

        for money in nums:
            new_rob = money + skip

            skip = max(skip, rob)
            rob = new_rob
        
        return max(rob, skip)
    
    # Overall analysis: time = O(n), space = O(1)
    # where n = number of houses
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        skip_first = self.rob_houses(nums[1:])
        skip_last = self.rob_houses(nums[:len(nums) - 1])

        return max(skip_first, skip_last)


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        ([2,3,2], 3),
        ([1,2,3,1], 4),
        ([1,2,3], 3)
    ]

    for i, (houses, expected) in enumerate(test_cases, 1):
        result = s.rob(houses)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"

    print("All test cases passed!")
