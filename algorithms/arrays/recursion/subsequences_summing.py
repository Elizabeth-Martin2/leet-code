from functools import lru_cache
import time

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
    DEBUG = True

    @staticmethod
    def _debug(*args, **kwargs):
        if Solution.DEBUG:
            print(*args, **kwargs)


    # Naive recursion analysis: time = O(2^n), space = O(n)
    # Note that space is O(n) because there are at most n layers of the recursion
    # call active at once (essentially a DFS)
    def countSubsequencesWithTargetSum_naive(self, nums: list[int], k: int) -> int:
        nums_len = len(nums)

        def helper(ind: int = 0, current: int = 0):
            if ind == nums_len:
                return 1 if current == k else 0

            return helper(ind + 1, current + nums[ind]) + helper(ind + 1, current)

        return helper(ind=0, current=0)

    # Optimized memoization analysis: time = O(n * k), space = O(n * k)
    def countSubsequencesWithTargetSum_memo(self, nums: list[int], k: int) -> int:
        nums_len = len(nums)

        @lru_cache(maxsize=None)
        def helper(ind: int = 0, current: int = 0):
            if ind == nums_len:
                return 1 if current == k else 0

            return helper(ind + 1, current + nums[ind]) + helper(ind + 1, current)

        return helper(ind=0, current=0)

    # Existence analysis: time = O(n * k), space = O(n * k)
    def existsSubsequenceWithTargetSum(self, nums: list[int], k: int) -> bool:
        nums_len = len(nums)

        @lru_cache(maxsize=None)
        def helper(ind: int = 0, current: int = 0):
            if ind == nums_len:
                return current == k

            return helper(ind + 1, current + nums[ind]) or helper(ind + 1, current)

        return helper()


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        ([4, 9, 2, 5, 1], 10, 2),
        ([4, 2, 10, 5, 1, 3], 5, 3),
        ([1, 2, 3, 2, 4, 1, 8], 12, 8)
    ]

    for i, (nums, k, expected) in enumerate(test_cases, 1):
        output = s.countSubsequencesWithTargetSum_memo(nums, k)
        assert output == expected, f"Memoized Test case {i} failed, expected {expected}, got {output}"

        output = s.countSubsequencesWithTargetSum_naive(nums, k)
        assert output == expected, f"Naive Test case {i} failed, expected {expected}, got {output}"

        output = s.existsSubsequenceWithTargetSum(nums, k)
        if expected > 0: assert output == True, f"Naive Test case {i} failed, expected {expected}, got {output}"
        else: assert output == False, f"Existence Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")

    print("Stress testing functions...")

    # Use below to test the difference between naive & memoized approaches
    nums = [1] * 25
    target = 10

    # Time naive version, time = O(2^n)
    start = time.time()
    result_naive = s.countSubsequencesWithTargetSum_naive(nums, target)
    end = time.time()
    print(f"Naive result = {result_naive}, time = {end - start:.4f} sec")

    # Time memoized version, time = O(n * k)
    start = time.time()
    result_memo = s.countSubsequencesWithTargetSum_memo(nums, target)
    end = time.time()
    print(f"Memoized result = {result_memo}, time = {end - start:.4f} sec")

    start = time.time()
    result_memo = s.existsSubsequenceWithTargetSum(nums, target)
    end = time.time()
    print(f"Existence result = {result_memo}, time = {end - start:.4f} sec")

    # Results when last run:
    # Naive result = 3268760, time = 4.4879 sec
    # Memoized result = 3268760, time = 0.0000 sec
    # Existence result = True, time = 0.0000 sec