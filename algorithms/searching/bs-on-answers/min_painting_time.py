class Solution: 
    """
    Given an array of board lengths (boards) and a number of painters (k)
    return the minimum amount of time required to paint all of the boards.

    Given: each unit of a board takes 1 unit of time to paint & painters
    will only paint the continuous sections of boards.

    Uses binary search to find the minimum amount of time required to
    complete the job.
    """

    # Analysis: time = O(n log(sum(boards))), space = O(1)
    # where n = len(boards)
    def findLargestMinDistance(self, boards:list, k:int):
        if k == len(boards):
            return max(boards)

        left, right = max(boards), sum(boards)

        # Function analysis: time = O(n), space = O(1)
        def can_paint(target:int) -> bool:
            current_sum, count = 0, 1

            for board_len in boards:
                if current_sum + board_len <= target:
                    current_sum += board_len
                else:
                    current_sum = board_len
                    count += 1
                    if count > k:
                        return False

            return True

        while left < right:
            mid = (left + right) // 2

            if can_paint(mid):
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([10, 20, 30, 40], 2, 60),
        ([6,5,6,10,9,2,3,5], 2, 27),
        ([5, 2, 1], 3, 5)
    ]

    for i, (boards, painters, expected) in enumerate(test_cases, 1):
        output = solution.findLargestMinDistance(boards, painters)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")