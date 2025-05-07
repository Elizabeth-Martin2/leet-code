class Solution:
    """
    Given an array of distinct integers (candidates) and a target integer (target),
    return a list of all unique combinations of candidates where the chosen
    numbers sum to target. You may return the combinations in any order.

    The same number may be chosen from candidates an unlimited number of times.
    Two combinations are unique if the frequency of at least one of the chosen
    numbers is different.

    LC. 39 Combination Sum
    """

    # Analysis: time = O(2^T), space = O(n)
    # where T = target
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates = sorted(candidates)
        num_candidates = len(candidates)
        res = []

        def helper(ind: int = 0, remaining: int = target, current: list[int] = []) -> None:
            if remaining == 0:
                res.append(current[:])
                return
            if remaining < 0 or ind == len(candidates):
                return

            for i in range(ind, num_candidates):
                if candidates[i] > remaining:
                    return
                current.append(candidates[i])
                helper(i, remaining - candidates[i], current)
                current.pop()

        helper()
        return res


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        ([2,3,6,7], 7, [[2,2,3],[7]]),
        ([2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]]),
        ([2], 1, [])
    ]

    for i, (candidates, target, expected) in enumerate(test_cases, 1):
        output = s.combinationSum(candidates, target)
        assert sorted(output) == sorted(expected), f"Optimized Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")