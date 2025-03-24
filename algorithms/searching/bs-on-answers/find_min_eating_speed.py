class Solution:
    """
    Returns the minimum number of bananas that must be eaten 
    per hour to finish all of them before the guards return in 
    a given number (h) of hours.

    Uses binary search to find the minimum number of hours.
    LC 875. Koko Eating Bananas
    """

    # Analysis: time = O(n log m), space = O(1)
    # where n = len(piles) and m = max(piles)
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)

        # Binary search time = O(log m)
        while left < right:
            mid = (left + right) // 2
            count = 0

            # Linear loop time = O(n)
            for pile in piles:
                count += (pile + mid - 1) // mid
            
            if count > h: # Eat faster
                left = mid + 1
            
            else: # Eat slower
                right = mid

        return left

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([3,6,7,11], 8, 4),
        ([30,11,23,4,20], 5, 30),
        ([30,11,23,4,20], 6, 23)
    ]

    for i, (piles, hours, expected) in enumerate(test_cases, 1):
        output = solution.minEatingSpeed(piles, hours)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")