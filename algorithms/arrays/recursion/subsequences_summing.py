class Solution:
    """
    Given an array nums and an integer k.Return the number of non-empty 
    subsequences of nums such that the sum of all elements in the 
    subsequence is equal to k.
    
    Example:
        Input : nums = [4, 9, 2, 5, 1] , k = 10
        Output : 2
        Explanation : The possible subsets with sum k are [9, 1] , [4, 5, 1].

    """

    # Analysis: time = O(2^n), space = O(n)
    # Note that space is O(n) because there are at most n layers of the recursion
    # call active at once (essentially a DFS)
    def countSubsequencesWithTargetSum(self, nums: list[int], k: int) -> int:
        nums_len = len(nums)

        def helper(ind: int = 0, current: int = 0):
            if ind == nums_len:
                return 1 if current == k else 0

            return helper(ind + 1, current + nums[ind]) + helper(ind + 1, current)

        return helper(ind=0, current=0)


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        ([4, 9, 2, 5, 1], 10, 2),
        ([4, 2, 10, 5, 1, 3], 5, 3),
        ([1, 2, 3, 2, 4, 1, 8], 12, 8)
    ]

    for i, (nums, k, expected) in enumerate(test_cases, 1):
        output = s.countSubsequencesWithTargetSum(nums, k)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")
