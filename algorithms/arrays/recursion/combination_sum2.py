class Solution:
    """
    Given a collection of candidate numbers (candidates) and a target number (target),
    find all unique combinations in candidates where the candidate numbers sum to target.

    Each number in candidates may only be used once in the combination.

    Note: The solution set must not contain duplicate combinations.

    LC. 40 Combination Sum 2
    """

    # Analysis: time = O(2^T), space = O(n)
    # where T = target
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates = sorted(candidates)
        num_candidates = len(candidates)
        res = []

        def helper(ind: int = 0, remaining: int = target, current: list[int] = []) -> None:
            if remaining == 0:
                # make a copy of current to avoid reference bugs
                res.append(current[:])
                return
            if remaining < 0 or ind == len(candidates):
                return

            for i in range(ind, num_candidates):
                if i > ind and candidates[i] == candidates[i - 1]:
                    continue # skip duplicates in same recursion level
                if candidates[i] > remaining:
                    break # no more reason to loop
                current.append(candidates[i])
                helper(i + 1, remaining - candidates[i], current)
                current.pop()

        helper()
        return res


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        ([10,1,2,7,6,1,5], 8, [[1,1,6],[1,2,5],[1,7],[2,6]]),
        ([2,5,2,1,2], 5, [[1,2,2],[5]]),
        ([2], 1, [])
    ]

    for i, (candidates, target, expected) in enumerate(test_cases, 1):
        output = s.combinationSum2(candidates, target)
        assert sorted(output) == sorted(expected), f"Optimized Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")