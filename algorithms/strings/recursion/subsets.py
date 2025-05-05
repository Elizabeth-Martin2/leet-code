class Solution:
    """
    Given an integer array nums of unique elements, return all
    possible subsets (the power set).

    The solution set must not contain duplicate subsets.

    LC. 78 Subsets
    """

    DEBUG = False

    @staticmethod
    def _debug(*args, **kwargs):
        if Solution.DEBUG:
            print(*args, **kwargs)
    
    # Analysis: time = O(2^n * n) [2^n subsets, n to copy each]
    #           space = O(2^n * n) [to store results]
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def _helper(index:int, current:list[int]) -> None:
            res.append(current[:])
            Solution._debug("current:", current)

            for i in range(index, len(nums)):
                current.append(nums[i])
                _helper(i + 1, current)
                current.pop()

        res = []
        _helper(0, [])
        return res
            

if __name__ == "__main__":
    s = Solution()

    test_cases = [
        ([0], [[],[0]]),
        ([1], [[],[1]]),
        ([1,2], [[],[1],[1,2],[2]]),
        ([1,2,3], [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]])
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        output = s.subsets(nums)
        assert sorted(output) == sorted(expected), f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")
