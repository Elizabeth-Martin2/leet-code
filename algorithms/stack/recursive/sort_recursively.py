class Solution:
    # Set DEBUG flag to true to enable print statements
    DEBUG = False

    # Analysis: time = O(n), space = O(n) [due to recursive call stack]
    def sort_stack(self, stack: list[int]) -> None:
        """
        Sorts the given stack in ascending order using recursion.
        You must not use any loop or extra data structure (like a second stack).
        Only recursion and stack operations (push/pop) are allowed.
        """

        # Helper function to insert numbers into the stack in a sorted order
        def insert_sorted(stack: list[int], num: int) -> None:
            if len(stack) == 0 or num >= stack[-1]:
                print(f"Appending {num} to stack") if Solution.DEBUG else None
                stack.append(num)
            else:
                temp = stack.pop()
                print(f"Popped {temp} from stack, calling insertion again...") if Solution.DEBUG else None
                insert_sorted(stack, num)

                print(f"Re-appending {temp} to the stack") if Solution.DEBUG else None
                stack.append(temp)

        # Helper function to recursively break down the stack
        def break_down_stack(stack:list[int]) -> None:
            if len(stack) != 0:
                num = stack.pop()

                print(f"Popped {num} from stack, calling break again") if Solution.DEBUG else None
                break_down_stack(stack)

                print("Done with breaking, moving to inserting...") if Solution.DEBUG else None
                insert_sorted(stack, num)

        print(f"Starting stack: {stack}...") if Solution.DEBUG else None
        break_down_stack(stack)


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        ([3, 1, 5, 2, 4], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1], [1])
    ]

    for i, (stack, expected) in enumerate(test_cases, 1):
        s.sort_stack(stack)
        assert stack == expected, f"Test case {i} failed, expected {expected}, got {stack}"

    print("All test cases passed!")