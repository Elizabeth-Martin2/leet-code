class Solution:
    """
    Given a list of package weights (weights), return the minimum weight
    capacity to ship all packages within the given number of days (days).

    Uses binary search to find the minimum weight.

    LC. 1011 Capacity to Ship Packages Within D Days
    """

    # Analysis: time = O(n log m), space = O(1)
    # where n = len(weights) i.e., number of packages
    # and m = sum(weights) - max(weights) => simplifies to sum(weights)
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        while left < right:
            max_weight = (left + right) // 2
            count_days, current_sum = 1,0 # days starts at 1 for final day
            
            for package in weights:
                if current_sum + package <= max_weight:
                    current_sum += package
                else:
                    count_days += 1
                    current_sum = package

            if count_days > days:
                left = max_weight + 1
            else:
                right = max_weight

        return left

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1,2,3,4,5,6,7,8,9,10], 5, 15),
        ([3,2,2,4,1,4], 3, 6),
        ([1,2,3,1,1], 4, 3)
    ]

    for i, (weights, days, expected) in enumerate(test_cases, 1):
        output = solution.shipWithinDays(weights, days)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")