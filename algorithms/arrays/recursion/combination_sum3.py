class Solution:
    """
    Given an integer n and another integer k, return a list of all possible ways to add
    k numbers to equal n.  Each number is only used once and only numbers 1 - 9 are allowed.

    LC. 216 Combination Sum 3
    """

    # Analysis: time = O(2^k), space = O(k)
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res = []

        def helper(total_nums: int = k, remaining: int = n, current: list[int] = [], num: int = 1) -> None:
            if total_nums == 0:
                if remaining == 0:
                    res.append(current[:])
                return
            if num > 9 or remaining < 0:
                return
            
            # Choice 1: Use the current number
            current.append(num)
            helper(total_nums - 1, remaining - num, current, num + 1)

            # Choice 2: Skip the current number
            current.pop()
            helper(total_nums, remaining, current, num + 1)
        
        helper()
        return sorted(res)


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        (3, 7, [[1,2,4]]),
        (3, 9, [[1,2,6],[1,3,5],[2,3,4]]),
        (9, 45, [[1,2,3,4,5,6,7,8,9]]),
        (4, 1, [])
    ]

    for i, (k, n, expected) in enumerate(test_cases, 1):
        output = s.combinationSum3(k, n)
        assert output == expected, f"Optimized Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")