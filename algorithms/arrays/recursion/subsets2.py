class Solution:
    """
    Given an integer array nums that may contain duplicates,
    return all possible subsets (the power set).

    The solution set must not contain duplicate subsets.
    Return the solution in any order.

    LC. 90 Subsets 2
    """

    # Analysis: time = O(2^n), space = O(n)
    # where n = length of nums
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums_len = len(nums)
        nums.sort()

        def helper(start: int = 0, current: list[int] = []) -> None:
            res.append(current[:]) # make a copy to avoid issues

            for i in range(start, nums_len):
                if i > start and nums[i] == nums[i - 1]:
                    continue # exclude duplicate subsets
                
                # Choice 1: include num 
                current.append(nums[i])
                helper(i + 1, current)
                # Choice 2: skip num
                current.pop() 

        helper()
        return sorted(res)


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        ([0], [[],[0]]),
        ([1,2], [[], [1], [1, 2], [2]]),
        ([1,2,2], [[],[1],[1,2],[1,2,2],[2],[2,2]])
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        output = s.subsetsWithDup(nums)
        assert output == expected, f"Optimized Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")