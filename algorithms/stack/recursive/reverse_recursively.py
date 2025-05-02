class Solution:
    # Set DEBUG flag to true to enable print statements
    DEBUG = False

    @staticmethod
    def _debug(*args, **kwargs):
        if Solution.DEBUG:
            print(*args, **kwargs)


    def reverse_stack(self, stack: list[int]) -> None:
        """
        Reverses the given stack using recursion.
        You must not use any loop or extra data structure (like a second stack).
        Only recursion and stack operations (push/pop) are allowed.
        """

        # Helper function to insert at the bottom of the stack
        # Note this is very inefficient, but required to meet recursion req's
        def insert_at_bottom(stack: list[int], num: int) -> None:
            if not stack:
                Solution._debug("Appending", num)
                stack.append(num)

            else:
                popped_num = stack.pop()
                Solution._debug("insertion: Popped", popped_num)

                insert_at_bottom(stack, num)
                stack.append(popped_num)

        # Analysis: time = O(n^2), space = O(n^2) [due to recursive call stack]
        def reverse_helper(stack: list[int]) -> None:
            if not stack:
                return

            num = stack.pop()
            Solution._debug("rev_helper: Popped", num)
            reverse_helper(stack)

            Solution._debug("Calling insert with num:", num)
            insert_at_bottom(stack, num)

        Solution._debug("Starting stack:", stack)
        reverse_helper(stack)


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        ([3, 1, 5, 2, 4], [4, 2, 5, 1, 3]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1], [1])
    ]

    for i, (stack, expected) in enumerate(test_cases, 1):
        s.reverse_stack(stack)
        assert stack == expected, f"Test case {i} failed, expected {expected}, got {stack}"
        Solution._debug("-------------------")

    print("All test cases passed!")