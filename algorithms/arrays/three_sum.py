class Solution:
    """Finds unique triplets in an array that sum to zero."""

    # Analysis: time = O(n^2), space = O(n)
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        """Returns a list of unique triplets where the sum of three numbers equals zero."""
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate values
            
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    # Avoid duplicate values
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return res


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),  # Case where multiple zeros exist
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        assert solution.three_sum(nums) == expected, f"Test case {i} failed"

    print("All test cases passed!")
