class Solution:
    """
    Given an integer array nums representing the amount of money of each house, and
    the knowledge that robbing two houses in a row will alert the police, return the
    maximum amount of money you can rob tonight without alerting the police.

    LC. 198 House Robber
    """

    # Analysis: time = O(n), space = O(1)
    # where n = number of houses
    def rob(self, nums: list[int]) -> int:
        rob, skip = 0, 0

        for money in nums:
            # rob this house + money from skipping last house
            new_rob = skip + money
            
            # skip this house and take maximum amount of robberies
            skip = max(skip, rob)

            rob = new_rob
        
        return max(rob, skip)



if __name__ == "__main__":
    s = Solution()

    test_cases = [
        ([1,2,3,1], 4),
        ([2,7,9,3,1], 12),
        ([2,1,1,2], 4)
    ]

    for i, (houses, expected) in enumerate(test_cases, 1):
        result = s.rob(houses)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"

    print("All test cases passed!")
