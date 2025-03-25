class Solution:
    """
    Return the target fibonacci number.
    """

    # Analysis: time = O(target), space = O(1)
    def fibonacci(self, target: int) -> int:
        if target == 0:
            return 0
        elif target == 1:
            return 1

        prev, current = 0, 1
        print("0: prev: NA, current: 0")
        print("1: prev: 0, current: 1")

        for i in range(2, target + 1):
            prev, current = current, prev + current
            print(f"{i}: prev: {prev}, current: {current}")
        
        print(f"fibonacci number {target} = {current}")
        return current


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13)
    ]

    for i, (target, expected) in enumerate(test_cases, 1):
        output = solution.fibonacci(target)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")